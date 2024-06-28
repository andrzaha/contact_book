from litellm import completion
import os
import yaml
import argparse


def read_script_file(script_path):
    with open(script_path, "r") as script_file:
        return script_file.read()


def generate_markdown(messages):
    """
    Generate additional details about the script using OpenAI and create a Markdown file.
    """
    print("Generating detailed markdown documentation...")
    response = completion(model="gpt-4o", messages=messages)
    return response["choices"][0]["message"]["content"]


def update_mkdocs_yml(markdown_file):
    with open("../mkdocs.yml", "r") as file:
        mkdocs_config = yaml.safe_load(file)

    if "nav" not in mkdocs_config:
        mkdocs_config["nav"] = []

    doc_entry = {
        os.path.basename(markdown_file).replace(".md", ""): os.path.basename(
            markdown_file
        )
    }

    if doc_entry not in mkdocs_config["nav"]:
        mkdocs_config["nav"].append(doc_entry)

    with open("../mkdocs.yml", "w") as file:
        yaml.safe_dump(mkdocs_config, file, indent=2)


def main(script_path, docs_dir):

    script_content = read_script_file(script_path)
    messages = [
        {"role": "system", "content": "You are a code documentation generator."},
        {
            "role": "user",
            "content": f"Generate a detailed markdown syntax documentation for the following Python script:\n\n{script_content}. Return only the documentation response and nothing else.",
        },
        {
            "role": "user",
            "content": "The documentation must include only the following sections. Heading 1: Function or Class Name. Heading 2: Parameters, Functionality, Flow, Output Format, Return Value, Example Usage, Additional Notes.",
        },
    ]
    markdown_content = generate_markdown(messages)
    markdown_file_name = os.path.basename(script_path).replace(".py", ".md")
    markdown_file_path = os.path.join(docs_dir, markdown_file_name)

    with open(markdown_file_path, "w") as markdown_file:
        markdown_file.write(markdown_content)

    update_mkdocs_yml(markdown_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate documentation for a Python script."
    )
    parser.add_argument("script_path", help="Path to the Python script")
    parser.add_argument(
        "--docs_dir",
        default="../docs",
        help="Path to the docs directory (default: ../docs)",
    )

    args = parser.parse_args()

    main(args.script_path, args.docs_dir)
