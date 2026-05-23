"""Translation module using googletrans to translate French words to English."""

# pip install googletrans==4.0.0-rc1

from googletrans import Translator


def translate_words(words, src_lang="fr", dest_lang="en"):
    """
    Translate a list of words from source language to destination language.

    Parameters:
        words     : list of strings to translate
        src_lang  : source language code (default: 'fr' for French)
        dest_lang : destination language code (default: 'en' for English)

    Returns:
        dict: {original_word: translated_word}
    """
    translator = Translator()

    # Build the dictionary using dict comprehension
    translations = {
        word: translator.translate(word, src=src_lang, dest=dest_lang).text
        for word in words
    }

    return translations


def main():
    """Main function to translate French words to English."""

    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

    print("=" * 50)
    print("  French → English Translation")
    print("=" * 50)

    result = translate_words(french_words)

    # Print the dictionary result
    print(result)

    # Print each translation clearly
    print("\n  Word by word:")
    for french, english in result.items():
        print(f"  {french:15} → {english}")


if __name__ == "__main__":
    main()