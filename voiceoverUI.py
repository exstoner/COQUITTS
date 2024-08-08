import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QComboBox, QHBoxLayout, QSizePolicy, QLineEdit, QMessageBox
from PySide6.QtCore import Slot, Qt

class VoiceoverApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voiceover Generator")
        self.setMinimumSize(400, 400)  # Set minimum size for the window

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)  # Add padding around the layout

        # Text input (QTextEdit for multi-line text)
        self.text_input = QTextEdit(self)
        self.text_input.setPlaceholderText("Enter text for the voiceover")
        self.text_input.setFixedHeight(200)  # Set a reasonable height for text input
        self.text_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(self.text_input)

        # Speaker selection
        speaker_layout = QHBoxLayout()
        speaker_label = QLabel("Choose a speaker:")
        speaker_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        speaker_layout.addWidget(speaker_label)

        self.speaker_combo = QComboBox(self)
        self.speaker_combo.addItems(['Abrahan Mack', 'Baldur Sanjin', 'Tanja Adelina', 'Viktor Menelaos', 'Chandra MacFarland'])
        self.speaker_combo.setFixedHeight(30)  # Adjust the combo box height
        speaker_layout.addWidget(self.speaker_combo)
        main_layout.addLayout(speaker_layout)

        # Output file name input
        self.output_input = QLineEdit(self)
        self.output_input.setPlaceholderText("Enter output file name (without extension)")
        self.output_input.setFixedHeight(40)  # Increase the height of the output input
        self.output_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_layout.addWidget(self.output_input)

        # Generate button (bigger and centered)
        self.generate_button = QPushButton("Generate", self)
        self.generate_button.setFixedHeight(50)  # Increase button height
        self.generate_button.setStyleSheet("font-size: 16px;")  # Make the font size larger
        self.generate_button.clicked.connect(self.generate_voiceover)
        main_layout.addWidget(self.generate_button)

        self.setLayout(main_layout)

    @Slot()
    def generate_voiceover(self):
        text = self.text_input.toPlainText()  # Correct method to get text from QTextEdit
        speaker_name = self.speaker_combo.currentText()
        output_name = self.output_input.text()
        output_file = f"output/{output_name}.wav"

        if not text or not output_name:
            return

        from TTS.api import TTS

        def transcribe_text(text, output_file, speaker_name, language='en'):
            tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
            tts.tts_to_file(
                text=text,
                file_path=output_file,
                speaker=speaker_name,
                language=language,
                split_sentences=True
            )

        transcribe_text(text, output_file, speaker_name)

        # Show message box indicating the process is complete
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Voiceover Complete")
        msg_box.setText(f"Voiceover Complete")
        msg_box.exec_()

        # Clear the input fields
        self.text_input.clear()
        self.output_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceoverApp()
    window.show()
    sys.exit(app.exec())
