Here’s the complete and updated `README.md` for your project:

```markdown
# Flight Data Project

This project processes and analyzes flight data stored in JSON files. The data is collected from a specified directory, cleaned, and analyzed to extract insights such as top destinations, flight durations, and cities with the highest passenger counts.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the project, you will need Python 3.x and some dependencies. Follow the steps below to set up the environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-data-project.git
   cd flight-data-project
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the data collection, processing, and analysis:

1. **Ensure the flight data files are available**:
   - Make sure the flight data JSON files are located in the directory specified by `FLIGHT_DATA_DIR`. You can configure this directory in the `constants/config.py` file.

2. **Run the scripts**:
   - **Data Generation Phase**:
     First, execute the **data generation** phase by running:
     ```bash
     python scripts/generate_data.py
     ```
     This script will generate and clean flight data, then store the cleaned JSON files in the `/tmp/flights/` directory.

   - **Data Analysis and Cleaning Phase**:
     Next, run the **data analysis and cleaning** phase by executing:
     ```bash
     python scripts/analyze_data.py
     ```
     This script will analyze the flight data, generate insights such as the top 25 destinations, and clean the data by removing any dirty records.

### Example Output:
```plaintext
Total records processed: 100
Total dirty records: 5
Average flight duration for top 25 destinations:
NYC       3250
LA        4000
...
95th percentile of flight duration for top 25 destinations:
NYC       4000
LA        4500
...
City with maximum passengers arrived: LA
City with maximum passengers left: NYC
```

## File Structure

```
flight_data_project/
├── /tmp/flights/                # Directory for generated flight JSON files (handled by the system)
├── scripts/                     # Contains the main scripts for data generation and analysis
│   ├── generate_data.py         # Script for data generation phase (collects and processes flight data)
│   └── analyze_data.py          # Script for the analysis and cleaning phase (analyzes and cleans the data)
├── tests/                       # Unit tests for various modules
│   ├── test_generate_data.py    # Unit tests for data generation
│   ├── test_analyze_data.py     # Unit tests for data analysis
│   ├── test_file_utils.py       # Unit tests for file utilities
│   └── test_data_utils.py       # Unit tests for data utilities
├── utils/                       # Utility modules
│   ├── file_utils.py            # Functions for reading/writing files
│   ├── logging_config.py        # Logger configuration
│   ├── custom_exceptions.py     # Custom exceptions
│   └── logger.py                # Logger functions
├── constants/                   # Configuration constants
│   ├── config.py                # Configuration file for file paths, etc.
├── requirements.txt             # List of dependencies
└── README.md                    # This file
```

## Testing

Unit tests are provided for the project. To run the tests:

1. Ensure you are in the project directory and have activated the virtual environment.
2. Run the tests with the following command:
   ```bash
   python -m unittest discover -s tests
   ```

This will run all the test cases in the `tests/` directory.

### Example Test Case
The tests are organized as follows:
- `test_generate_data.py`: Unit tests for data generation.
- `test_analyze_data.py`: Unit tests for data analysis (e.g., top destinations).
- `test_file_utils.py`: Unit tests for file utilities (e.g., reading JSON files).
- `test_data_utils.py`: Unit tests for data cleaning and processing utilities.

## Contributing

If you'd like to contribute to this project, feel free to open a pull request. Please ensure that your contributions are well-tested and include appropriate documentation.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Key Updates:
- **Complete Instructions**: The steps for installing dependencies, running scripts, and analyzing the output are clear and organized.
- **Usage**: The usage section has been clarified, showing how to run both the **data generation** and **analysis** phases.
- **File Structure**: The updated project structure reflects the changes and the paths to the scripts and directories.
- **Testing**: Added section on how to run unit tests using `unittest`.

This should provide clear instructions for setting up, running, and contributing to the project!