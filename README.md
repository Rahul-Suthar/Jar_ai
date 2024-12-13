# Jar AI

Jar AI is a voice-controlled personal assistant built with Python, leveraging Speech Recognition and Text-to-Speech capabilities. Jar AI can process simple commands to open tabs, play songs, and more, making your daily tasks more efficient.

## Features
- **Voice Command Recognition**: Uses `speech_recognition` to listen to and process user commands.
- **Browser Automation**: Opens specified tabs or plays songs using `webbrowser`.
- **Text-to-Speech**: Provides voice feedback using `pyttsx3`.
- **Customizable Commands**: Easily extend the functionality with new commands.

## Technologies Used
- Python
- `speech_recognition` for processing voice inputs.
- `pyttsx3` for text-to-speech output.
- `webbrowser` for automating browser actions.
- Custom `daily` module for predefined tabs and songs.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Rahul-Suthar/Jar_ai.git
   cd Jar_ai
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv Jarenv
   source Jarenv/bin/activate # On Windows: Jarenv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file:
   ```
   API_KEY=<your_api_key_if_applicable>
   ```

## Usage
1. Run the program:
   ```bash
   python main.py
   ```

2. Speak a command such as:
   - "Open YouTube"
   - "Play SongName"

3. Jar AI will respond to your voice command and perform the requested action.

## Example Commands
- **Opening Tabs**: Say `"Open YouTube"`. The program will open YouTube in your default browser.
- **Playing Songs**: Say `"Play SongName"`. Jar AI will look up the song in the predefined list and play it.

## Customization
- Add your own tabs or songs in the `daily.py` file. For example:
   ```python
   Tabs = {
       "youtube": "https://www.youtube.com",
       "github": "https://github.com"
   }

   Songs = {
       "despacito": "<song_link>"
   }
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Rahul Suthar  
[GitHub Profile](https://github.com/Rahul-Suthar)

---

**Note**: Ensure your microphone permissions are enabled, and dependencies are installed correctly for seamless functionality.
