import os
import sys
import subprocess
import shutil

def create_project(project_name, directory):
    # Define the target directory
    target_directory = os.path.join(os.path.expanduser("~"), "Documents", "CMake Projects")
    os.makedirs(target_directory, exist_ok=True)  # Create target directory if it doesn't exist

    # Create the new project directory in the original location
    project_dir = os.path.join(directory, project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Create the CMakeLists.txt file with the given template
    cmake_content = f"""cmake_minimum_required(VERSION 3.28)
project({project_name})
add_executable({project_name}_app main.cpp)
target_sources({project_name}_app PRIVATE main.cpp)
"""
    with open(os.path.join(project_dir, "CMakeLists.txt"), "w") as cmake_file:
        cmake_file.write(cmake_content)

    # Create the main.cpp file with basic Hello World content
    cpp_content = f"""#include <iostream>

int main() 
{{
    std::cout << "Hello, {project_name}!" << std::endl;
    return 0;
}}
"""
    with open(os.path.join(project_dir, "main.cpp"), "w") as cpp_file:
        cpp_file.write(cpp_content)

    print(f"Project {project_name} created successfully in {project_dir}")

    # Move the project directory to the target location
    new_project_dir = os.path.join(target_directory, project_name)
    shutil.move(project_dir, new_project_dir)
    print(f"Project moved to {new_project_dir}")

    # Ask the user if they want to generate the project files
    generate = input("Do you want to generate the project with CMake now? (y/n): ").strip().lower()
    if generate != "y":
        print("Skipping the generation step.")
        os.startfile(new_project_dir)  # Open the project folder
        return

    # Try generating the project with CMake
    try:
        print("Running 'cmake -Bbuild' to generate project files...")
        subprocess.check_call(["cmake", "-Bbuild"], cwd=new_project_dir)
        print("CMake generation succeeded.")

        # Ask the user if they want to build the project
        build = input("Do you want to build the project now? (y/n): ").strip().lower()
        if build == "y":
            print("Running 'cmake --build build' to build the project...")
            subprocess.check_call(["cmake", "--build", "build"], cwd=new_project_dir)
            print("Build completed successfully.")
        else:
            print("Skipping the build process.")
    except subprocess.CalledProcessError as e:
        print(f"Error during CMake generation or build: {e}")
        sys.exit(1)

    # Open the project directory after all operations
    os.startfile(new_project_dir)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_project.py <project_name> <directory>")
        sys.exit(1)

    project_name = sys.argv[1]
    directory = sys.argv[2]
    create_project(project_name, directory)
