import subprocess
import shlex

def run_script(script_name, args):
    """
    Run a Python script with given arguments.
    
    Args:
        script_name (str): Name of the script to run
        args (list): List of command line arguments
    """
    try:
        # Convert the argument string into properly quoted arguments
        processed_args = []
        for arg in args:
            if isinstance(arg, str):
                # Split the argument if it contains spaces
                processed_args.extend(shlex.split(arg))
            else:
                processed_args.append(str(arg))

        command = ['python', script_name] + processed_args
        
        print(f"\nRunning {script_name} with arguments:")
        print(f"Command: {' '.join(command)}\n")
        
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        print(f"Output of {script_name}:\n{result.stdout}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:")
        print(f"Exit code: {e.returncode}")
        print(f"Error output:\n{e.stderr}")
    except Exception as e:
        print(f"Unexpected error running {script_name}:")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Define base arguments
    video_name = '6b1d7ac3-8092-4235-b9c4-82b64fc3708e_karri-nmoukrk2u@00014_FHD_6_0_24.mp4'

    video_base = video_name.split('.mp4')[0]
    video_file = f"/efs/ala/data/gen_videos_ph2/{video_name}"
    reference = f"output/{video_base}"
    data_dir = f"output/{video_base}"

    # Create properly formatted argument list
    args = [
        f"--videofile {video_file}",
        f"--reference {reference}",
        f"--data_dir {data_dir}"
    ]

    # Define scripts to run with their arguments
    scripts = [
        'run_pipeline.py',
        'run_syncnet.py',
        'run_visualise.py'
    ]

    # Run each script
    for script in scripts:
        run_script(script, args)