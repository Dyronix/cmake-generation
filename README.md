# Project Generator Setup

This repository contains scripts to help you generate a new CMake project.

## Prerequisites

- **Windows OS**: Ensure you are using a Windows environment.
- **Python**: Make sure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/). Verify the installation by running `python --version` in the Command Prompt.
- **CMake**: Ensure CMake is installed. You can download it from [cmake.org](https://cmake.org/download/). Verify the installation by running `cmake --version`.

## Setup Instructions

Follow these steps to set up the project generator on your local machine:

### 1. Clone the Repository

Clone this repository to your local machine using Git or download the ZIP file.

```bash
git clone https://github.com/Dyronix/cmake-generation.git
```

### 2. Copy Scripts to `C:/Scripts`

1. Copy the `make_project.bat` and `create_project.py` files from this repository.
2. Create the directory `C:/Scripts` if it doesn't already exist:


   ```bash
   mkdir C:\Scripts
   ```

### 3. Set Up Environment Variables

To ensure Windows recognizes the scripts when you run commands from the address bar in File Explorer, follow these steps:

1. Press `Win + R`, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab and click on **Environment Variables**.
3. Under **System variables**, find and select the **Path** variable, then click **Edit**.
4. Click **New** and add the path to your scripts directory:

   C:\Scripts

5. Click **OK** to close all dialog boxes.
6. Restart PC

### 4. Running the Script

1. Open **File Explorer** and navigate to the directory where you want to create your new project.
2. Click on the address bar, type `make_project <project_name>`, and press Enter. This will open the Command Prompt at the current directory and run the script.

### 5. Interaction with the Script

- The script will prompt you with two questions:
  1. **run CMake project generation?** (Type `yes` or `no`)
  2. **Do you want to build the project (if you ran CMake)?** (Type `yes` or `no`)
- Finally, it will open the folder of the generated project.

### 6. Troubleshooting

- If you encounter a "python is not recognized" error, ensure Python is installed and added to your system PATH.
- If CMake commands are not recognized, verify that CMake is installed and added to your PATH as well.
- Ensure that you copied the scripts to the correct directory (C:/Scripts) and that the path is correctly set in the environment variables.

## Conclusion

You now have a working setup that allows you to generate new CMake projects on the fly. Feel free to customize the scripts to fit your project's needs!