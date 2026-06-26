from gtts import gTTS

LANGUAGE_MAP = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Malayalam": "ml"
}

def generate_narration(
    text,
    language="English",
    output_file="outputs/trailer_voice.mp3"
):

    lang_code = LANGUAGE_MAP.get(language, "en")

    # Limit narration length
    text = text[:2500]

    tts = gTTS(
        text=text,
        lang=lang_code,
        slow=False
    )

    tts.save(output_file)

    print("✅ Narration Saved")

    return output_file