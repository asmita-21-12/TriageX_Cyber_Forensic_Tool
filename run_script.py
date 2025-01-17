import subprocess
import os
import time

# Path to the capture and analysis scripts
capture_script = 'capture_packet.py'
analysis_script = 'anomaly_detection.py'

# Path to the PCAP file (make sure this matches the file generated by capture_packets.py)
pcap_file = 'capture.pcap'

def run_capture():
    """
    Run the packet capture script to generate the PCAP file.
    """
    print("Starting packet capture...")
    try:
        subprocess.run(['python', capture_script], check=True)
        print("Packet capture completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {capture_script}: {e}")
        return False
    return True

def run_analysis():
    """
    Run the anomaly detection script to analyze the generated PCAP file.
    """
    print("Starting anomaly detection...")
    try:
        subprocess.run(['python', analysis_script], check=True)
        print("Anomaly detection completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {analysis_script}: {e}")

def main():
    # Ensure the PCAP file does not exist before capturing
    if os.path.exists(pcap_file):
        os.remove(pcap_file)
    
    if run_capture():
        # Wait a bit to ensure the PCAP file is fully written
        time.sleep(5)
        run_analysis()

if __name__ == "__main__":
    main()