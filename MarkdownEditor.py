
formatters = ["ordered-list", "unordered-list", "plain", "bold", "italic", "header", "link", "inline-code", "new-line", "!help", "!done"]
help_message = """Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done"""
format_error_message = "Unknown formatting type or command"
range_error_message = "The level should be within the range of 1 to 6"
list_error_message = "The number of rows should be greater than zero"

markdown = []
result = ""
output = ""
level = 0

while True:
    formatter = input("Choose a formatter: ")
    if formatter == "!help":
        print(help_message)
    elif formatter == "!done":
        with open("output.md", "w") as f:
            f.write(output)
        break
    elif formatter not in formatters:
        print(format_error_message)
    else:
        if formatter == "plain":
            text = input("Text: ")
            result = text
        elif formatter == "bold":
            text = input("Text: ")
            result = "**" + text + "**"
        elif formatter == "italic":
            text = input("Text: ")
            result = "*" + text + "*"
        elif formatter == "header":
            while True:
                level = int(input("Level: "))
                if level not in range(1, 7):
                    print(range_error_message)
                    continue
                break
            text = input("Text: ")
            result = level * "#" + " " + text + "\n"
        elif formatter == "link":
            label = input("Label: ")
            url = input("URL: ")
            result = f"[{label}]({url})"
        elif formatter == "inline-code":
            text = input("Text: ")
            result = "`" + text + "`"
        elif formatter == "new-line":
            result = "\n"
        elif formatter == "ordered-list":
            while True:
                row_count = int(input("Number of rows: "))
                if not row_count > 0:
                    print(range_error_message)
                    continue
                break
            elements = []
            for i in range(1, row_count + 1):
                element = input(f"Row #{i}: ")
                e = f"{i}. {element}"
                elements.append(e)
            result = "\n".join(elements) + "\n"
        elif formatter == "unordered-list":
            while True:
                row_count = int(input("Number of rows: "))
                if not row_count > 0:
                    print(range_error_message)
                    continue
                break
            elements = []
            for i in range(1, row_count + 1):
                element = input(f"Row #{i}: ")
                e = f"* {element}"
                elements.append(e)
            result = "\n".join(elements) + "\n"
        markdown.append(result)
        output = "".join(markdown)
        print(output)
