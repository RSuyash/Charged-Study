const { App, PluginSettingTab, Setting, Notice } = require('obsidian');

// --- Default Settings ---
const DEFAULT_SETTINGS = {
    websocketUrl: 'ws://localhost:8080', // Kept for potential future use or fallback
    promptPrefix: '',
    sendContext: true,
    maxHistoryLength: 100,
    createNoteFolder: '',
    insertTemplate: '> {response}',
    chatHistory: [],
    geminiApiKey: '', // Added for Direct Gemini
    geminiModel: 'gemini-pro' // Added for Direct Gemini
};

class WebappDashboardSettingTab extends PluginSettingTab {
    /** @param {App} app */
    /** @param {import('./main').WebappDashboardPlugin} plugin */
	constructor(app, plugin) {
		super(app, plugin);
		this.plugin = plugin;
	}

	display() {
		const {containerEl} = this;
		containerEl.empty();
		containerEl.createEl('h2', {text: 'Webapp Dashboard Settings'});

        containerEl.createEl('h3', { text: 'Gemini API' });
        new Setting(containerEl)
            .setName('Gemini API Key')
            .setDesc('Your Google AI Gemini API Key. Stored locally.')
            .addText(text => text
                .setPlaceholder('Enter API Key')
                .setValue(this.plugin.settings.geminiApiKey)
                .onChange(async (value) => {
                    this.plugin.settings.geminiApiKey = value.trim();
                    await this.plugin.saveSettings();
                }));
        new Setting(containerEl)
            .setName('Gemini Model')
            .setDesc('Select the Gemini model to use.')
            .addDropdown(dropdown => {
                dropdown
                    .addOption('gemini-pro', 'Gemini Pro')
                    .addOption('gemini-1.5-flash-latest', 'Gemini 1.5 Flash')
                    .addOption('gemini-1.5-pro-latest', 'Gemini 1.5 Pro')
                    .addOption('gemini-ultra', 'Gemini Ultra (Experimental)')
                    .addOption('gemini-pro-vision', 'Gemini Pro Vision (Experimental)')
                    .setValue(this.plugin.settings.geminiModel || DEFAULT_SETTINGS.geminiModel)
                    .onChange(async (value) => {
                        this.plugin.settings.geminiModel = value;
                        await this.plugin.saveSettings();
                    });
            });

        containerEl.createEl('h3', { text: 'Chat Behavior' });
        new Setting(containerEl)
            .setName('Prompt Prefix')
            .setDesc('Prepend text to messages.').addTextArea(t => t.setPlaceholder('e.g., Act as...').setValue(this.plugin.settings.promptPrefix).onChange(async (v) => { this.plugin.settings.promptPrefix = v; await this.plugin.saveSettings(); }));
        new Setting(containerEl).setName('Send Context').setDesc('Include active note name.').addToggle(t => t.setValue(this.plugin.settings.sendContext).onChange(async (v) => { this.plugin.settings.sendContext = v; await this.plugin.saveSettings(); }));
        new Setting(containerEl).setName('Insert Template').setDesc('Template for inserting responses ({response}).').addText(t => t.setPlaceholder(DEFAULT_SETTINGS.insertTemplate).setValue(this.plugin.settings.insertTemplate).onChange(async (v) => { this.plugin.settings.insertTemplate = v || DEFAULT_SETTINGS.insertTemplate; await this.plugin.saveSettings(); }));

        containerEl.createEl('h3', { text: 'History & Export' });
        new Setting(containerEl)
            .setName('Maximum History Length')
            .setDesc('Messages to keep (0 for unlimited).')
            .addText(text => text
                .setPlaceholder(String(DEFAULT_SETTINGS.maxHistoryLength))
                .setValue(String(this.plugin.settings.maxHistoryLength))
                .onChange(async (value) => {
                    const num = parseInt(value, 10);
                    this.plugin.settings.maxHistoryLength = (isNaN(num) || num < 0) ? DEFAULT_SETTINGS.maxHistoryLength : num;
                    if (this.plugin.settings.chatHistory.length > this.plugin.settings.maxHistoryLength) {
                        this.plugin.settings.chatHistory = this.plugin.settings.chatHistory.slice(-this.plugin.settings.maxHistoryLength);
                    }
                    await this.plugin.saveSettings();
                }));
        new Setting(containerEl)
            .setName('Note Folder')
            .setDesc('Folder for created notes (blank for root).')
            .addText(text => text
                .setPlaceholder('e.g., Chats/')
                .setValue(this.plugin.settings.createNoteFolder)
                .onChange(async (value) => {
                    this.plugin.settings.createNoteFolder = value.trim().replace(/\\/g, '/').replace(/\/$/, '');
                    await this.plugin.saveSettings();
                }));

        new Setting(containerEl)
            .setName('Clear Chat History')
            .setDesc('Permanently delete the saved chat history.')
            .addButton(button => button
                .setButtonText('Clear History')
                .setWarning()
                .onClick(async () => {
                    if (confirm('Are you sure you want to clear the chat history? This cannot be undone.')) {
                        this.plugin.settings.chatHistory = [];
                        await this.plugin.saveSettings();
                        new Notice('Chat history cleared.');
                        this.app.workspace.trigger('webapp-dashboard:clear-history');
                    }
                }));
	}
}

module.exports = { WebappDashboardSettingTab, DEFAULT_SETTINGS };