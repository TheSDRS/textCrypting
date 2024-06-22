def stripText(textToStrip: str):
    if textToStrip.startswith("'") or textToStrip.startswith('"'):
        if textToStrip.endswith("'") or textToStrip.endswith('"'):
            textToStrip = textToStrip.removeprefix(textToStrip[0])
            textToStrip = textToStrip.removesuffix(textToStrip[len(textToStrip) - 1])
            return textToStrip
