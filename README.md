# 📚 Children's Fiction Story Generator

A Python-based story generator that creates engaging children's fiction stories using AI. This project generates 10-chapter stories specifically designed for children aged 10-16 years old.

## 🎯 Story Requirements

- **Genre**: Children's Fiction (Chapter Book)
- **Target Age**: 10-16 years old
- **Format**: 10 chapters
- **Characters**: Leo, Zodiac, and other potential victims
- **Style**: Famous fiction writer for children with abundant vocabulary
- **Goal**: Create a top-selling children's book

## 🚀 Features

- **AI-Powered Story Generation**: Uses Google's Gemini Pro 2.5 model
- **Structured Output**: Generates complete story outlines and chapters
- **Multiple Formats**: Saves stories in Markdown, JSON, and individual chapter files
- **Professional Quality**: Designed to meet publishing standards for children's literature

## 📋 Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Internet connection for API access

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/QO2021/StoryTelling.git
   cd StoryTelling
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
   
   Or set it as an environment variable in your system.

## 🎭 Usage

### Running the Story Generator

```bash
python story_generator.py
```

The script will:
1. Prompt for your Gemini API key (if not set as environment variable)
2. Generate a complete story outline
3. Create 10 chapters with rich, vivid storytelling
4. Save all content in multiple formats

### Output Files

The generator creates several output files:
- `{timestamp}_full_story.md` - Complete story in Markdown format
- `{timestamp}_story_outline.json` - Story structure and chapter summaries
- `{timestamp}_chapters/` - Directory containing individual chapter files

## 📖 Story Structure

Each generated story follows this structure:
1. **Title and Synopsis** - Engaging introduction
2. **Chapter 1-10** - Progressive story development
3. **Character Development** - Growth of Leo, Zodiac, and supporting characters
4. **Plot Progression** - Each chapter advances the story meaningfully

## 🔧 Customization

You can modify the story generation by editing the prompts in `story_generator.py`:
- Change character names or descriptions
- Adjust story themes or settings
- Modify chapter length requirements
- Update target age group specifications

## 📚 Example Output

The generator creates stories with:
- Rich, descriptive language
- Age-appropriate content
- Engaging dialogue and action
- Compelling plot twists
- Professional writing quality

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Google Gemini AI for providing the language model
- The children's literature community for inspiration
- All contributors and users of this project

---

**Happy Storytelling! 📖✨**
