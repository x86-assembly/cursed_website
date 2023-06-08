
# Cursed WebDev Builder

The Cursed WebDev Builder is a Python script that converts JSON data into HTML markup. It provides a unique approach to generating HTML content by defining the structure and attributes of elements using JSON.

**Note: This project is purely for fun and does not have a practical use case. It is not intended for production use.**

## Usage

To use the Cursed WebDev Builder, follow the steps below:

1. Create a JSON file (`index.json`) inside the `src` directory. This file will define the structure of your HTML page.

2. Define the structure of your HTML page using JSON. The JSON structure should include the following elements: `type`, `content`, and `attributes`.

   - `type` (string): Specifies the HTML tag type for the element.
   - `content` (array): Contains the content of the element. Each item in the array represents a nested element or a string value.
   - `attributes` (object): Specifies the attributes for the element.

   Here's an example JSON structure:

   ```json
   {
       "type": "div",
       "content": [
           {
               "type": "h1",
               "content": ["Welcome to My Website"]
           },
           {
               "type": "p",
               "content": ["This is a paragraph."]
           },
           {
               "type": "img",
               "content": [],
               "attributes": {
                   "src": "https://files.codemania.net/example/images/example_dark.png",
                   "alt": "An image"
               }
           }
       ],
       "attributes": {}
   }
   ```

   The example above demonstrates adding an image (`img`) element with the `src` and `alt` attributes.

   **Note:** The `content` tag of an element must be an array. If the element has only one content item, enclose it in an array.

3. Run the Python script `build.py` using the following command:

   ```shell
   python build.py
   ```

   The script will convert the JSON data into HTML markup and save it to the `build/index.html` file.

4. Open the `build/index.html` file in a web browser to view the generated HTML page.

## Customization

To customize the HTML page, you can modify the `src/index.json` file. Add or remove elements, update the attributes, and change the content as desired. Each time you make changes, run the `build.py` script to generate the updated HTML file.

## License

The Cursed WebDev Builder is released under the MIT License. See the `LICENSE` file for more details.
