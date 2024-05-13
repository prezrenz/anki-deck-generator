from google_speech import Speech


def fix_format(pattern, changeTo, input):
    print(input)
    splitted = input.split(pattern)
    fixedFormat = "{}" + changeTo + "{}"
    return fixedFormat.format(splitted[0], splitted[1])


def generate_voice(input, output, lang):
    speech = Speech(input, lang)
    speech.save(output)


def format_text(input):
    formattedText = ""

    for each in input:
        formattedLine = fix_format(" - ", ";", each)
        formattedText += formattedLine

    return formattedText


def output_voice(input, outputDir, lang):
    for line in input.splitlines():
        word = line.split(";")
        output = outputDir+word[0]+".mp3"
        generate_voice(word[0], output, lang)


def output_anki_txt(input, outputDir):
    output = outputDir+"anki-import.txt"
    output = open(output, "w", encoding='utf-8')

    for line in input.splitlines():
        print(line)
        splitted = line.split(";")

        line += "[sound:{}.mp3]".format(splitted[0])
        output.write(line+"\n")

    output.close()


if __name__ == '__main__':
    input = open("input.txt", "r+", encoding='utf-8')
    outputDir = "output/"

    formattedText = format_text(input)
    output_voice(formattedText, outputDir, "ko")
    output_anki_txt(formattedText, outputDir)

    input.close()

