import os

print("\n1. ")
os.system("cd ~/Downloads")
os.system("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin")
os.system("sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600")
print("-------------------------------------------------------")
print("\n2. ")
os.system("wget https://developer.download.nvidia.com/compute/cuda/11.4.1/local_installers/cuda-repo-ubuntu2004-11-4-local_11.4.1-470.57.02-1_amd64.deb")
os.system("sudo dpkg -i cuda-repo-ubuntu2004-11-4-local_11.4.1-470.57.02-1_amd64.deb")
print("-------------------------------------------------------")
print("\n3. ")
os.system("sudo apt-key add /var/cuda-repo-ubuntu2004-11-4-local/7fa2af80.pub")
os.system("sudo apt-get update")
os.system("sudo apt-get update")
os.system("sudo apt-get -y install cuda")
print("-------------------------------------------------------")








