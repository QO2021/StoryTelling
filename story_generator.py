#!/usr/bin/env python3
"""
Children's Fiction Story Generator
Generates a 10-chapter story for children aged 10-16 with characters Leo and Zodiac.
"""

import os
import json
import datetime
from pathlib import Path

# Try to import google.generativeai, install if not available
try:
    import google.generativeai as genai
except ImportError:
    print("Installing google-generativeai...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

class StoryGenerator:
    """Generates children's fiction stories with the specified requirements."""
    
    def __init__(self, model):
        self.model = model
        
    def generate_story_outline(self):
        """Generate a story outline with 10 chapters."""
        
        outline_prompt = """
You are a famous fiction writer for children. You have an abundant vocabulary.

Create a detailed story outline for a chapter book with 10 chapters. The story should be for children aged 10 to 16 years old.

Characters:
- Leo: The main protagonist
- Zodiac: A mysterious character
- Other potential victims: Supporting characters

Requirements:
- Tell the story interestingly and vividly
- The story should be famous as a top seller in Children's books
- Each chapter should have a clear purpose and advance the plot
- Include character development and engaging plot twists
- Make it suitable for the target age group

Provide the output in JSON format with the following structure:
{
  "title": "Story Title",
  "synopsis": "Brief story summary (2-3 sentences)",
  "chapters": [
    {
      "chapter_number": 1,
      "chapter_title": "Chapter Title",
      "summary": "Brief chapter summary (1-2 sentences)"
    }
  ]
}

Ensure the JSON is valid and can be directly parsed. Do not include any other text outside the JSON.
"""
        
        try:
            response = self.model.generate_content(outline_prompt)
            response_text = response.text.strip()
            
            # Clean the response text to ensure it's valid JSON
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            response_text = response_text.strip()
            
            data = json.loads(response_text)
            return data
            
        except Exception as e:
            print(f"❌ Error generating story outline: {e}")
            return None
    
    def generate_chapter(self, chapter_info, story_context):
        """Generate a full chapter based on the outline."""
        
        chapter_prompt = f"""
You are a famous fiction writer for children. You have an abundant vocabulary.

Write Chapter {chapter_info['chapter_number']}: {chapter_info['chapter_title']}

Story Context:
{story_context}

Chapter Summary:
{chapter_info['summary']}

Requirements:
- Write in a vivid, engaging style suitable for children aged 10-16
- Use rich, descriptive language that paints pictures in the reader's mind
- Include dialogue, action, and character development
- Make it approximately 1500-2000 words
- End with a hook that makes readers want to continue
- Use markdown formatting with proper chapter headings

Write the complete chapter:
"""
        
        try:
            response = self.model.generate_content(chapter_prompt)
            return response.text.strip()
            
        except Exception as e:
            print(f"❌ Error generating chapter {chapter_info['chapter_number']}: {e}")
            return f"Error generating chapter {chapter_info['chapter_number']}"
    
    def generate_full_story(self):
        """Generate the complete story with all 10 chapters."""
        
        print("🎭 Generating story outline...")
        outline = self.generate_story_outline()
        
        if not outline:
            print("❌ Failed to generate story outline")
            return None
        
        print(f"📖 Story Title: {outline['title']}")
        print(f"📝 Synopsis: {outline['synopsis']}")
        print(f"📚 Total Chapters: {len(outline['chapters'])}")
        
        # Create story context for chapter generation
        story_context = f"""
Title: {outline['title']}
Synopsis: {outline['synopsis']}

Main Characters:
- Leo: The main protagonist
- Zodiac: A mysterious character
- Other supporting characters as needed
"""
        
        full_story = f"# {outline['title']}\n\n"
        full_story += f"*{outline['synopsis']}*\n\n"
        full_story += "---\n\n"
        
        # Generate each chapter
        for i, chapter in enumerate(outline['chapters']):
            print(f"📝 Generating Chapter {chapter['chapter_number']}: {chapter['chapter_title']}...")
            
            chapter_content = self.generate_chapter(chapter, story_context)
            full_story += chapter_content + "\n\n---\n\n"
            
            # Add chapter context for future chapters
            story_context += f"\nChapter {chapter['chapter_number']}: {chapter['chapter_title']} - {chapter['summary']}"
        
        return full_story, outline

def main():
    """Main function to run the story generator."""
    
    # Configuration - API Key Setup
    gemini_api_key = os.environ.get('GEMINI_API_KEY')
    if not gemini_api_key:
        gemini_api_key = input("Enter your Gemini API key: ")
    
    if not gemini_api_key:
        print("❌ GEMINI_API_KEY not found. Please set it as an environment variable or enter it when prompted.")
        return
    
    # Configure Gemini
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')
    
    print("🤖 Gemini Pro 2.5 model initialized successfully!")
    print("📝 Ready to generate your children's fiction story!")
    
    # Initialize story generator
    story_generator = StoryGenerator(model)
    
    # Generate the complete story
    print("🚀 Starting story generation...")
    print("This may take several minutes as we generate 10 chapters...")
    print("="*60)
    
    try:
        full_story, outline = story_generator.generate_full_story()
        
        if full_story:
            print("\n🎉 Story generation completed successfully!")
            print("="*60)
            
            # Save the story to files
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Save full story
            with open(f"{timestamp}_full_story.md", "w", encoding="utf-8") as f:
                f.write(full_story)
            print(f"\n💾 Full story saved to: {timestamp}_full_story.md")
            
            # Save outline
            with open(f"{timestamp}_story_outline.json", "w", encoding="utf-8") as f:
                json.dump(outline, f, indent=2, ensure_ascii=False)
            print(f"💾 Story outline saved to: {timestamp}_story_outline.json")
            
            # Save individual chapters
            chapters_dir = Path(f"{timestamp}_chapters")
            chapters_dir.mkdir(exist_ok=True)
            
            chapters = full_story.split("---")
            for i, chapter in enumerate(chapters[1:], 1):  # Skip the first split (title and synopsis)
                if chapter.strip():
                    chapter_filename = f"chapter_{i:02d}.md"
                    chapter_path = chapters_dir / chapter_filename
                    
                    with open(chapter_path, "w", encoding="utf-8") as f:
                        f.write(chapter.strip())
                    
                    print(f"   💾 Saved: {chapter_filename}")
            
            print(f"\n📂 All chapters saved to: {chapters_dir}")
            
            # Display statistics
            word_count = len(full_story.split())
            char_count = len(full_story)
            print(f"\n📊 Story Statistics:")
            print(f"   📝 Total Words: {word_count:,}")
            print(f"   📄 Total Characters: {char_count:,}")
            print(f"   📚 Total Chapters: {len(outline['chapters'])}")
            
            # Display story preview
            preview_length = 1000
            preview = full_story[:preview_length] + "..." if len(full_story) > preview_length else full_story
            print(f"\n📖 Story Preview:\n{preview}")
            
        else:
            print("❌ Story generation failed")
            
    except Exception as e:
        print(f"❌ Error during story generation: {e}")
        print("Please check your API key and try again.")

if __name__ == "__main__":
    main()
