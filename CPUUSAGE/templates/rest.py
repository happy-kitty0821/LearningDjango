import psutil
import platform

# Get total RAM (in bytes) and convert to GB
total_ram_gb = psutil.virtual_memory().total / (1024**3)

# Get CPU count
cpu_count = psutil.cpu_count(logical=False)  # physical CPU count
logical_cpu_count = psutil.cpu_count(logical=True)  # logical CPU count

# Get CPU frequency
cpu_freq = psutil.cpu_freq()

# Get CPU name and version
cpu_name = platform.processor()
cpu_version = platform.version()

# Get host OS
host_os = platform.system()

print("Total RAM: {:.2f} GB".format(total_ram_gb))
print("Physical CPU count:", cpu_count)
print("Logical CPU count:", logical_cpu_count)
print("CPU Frequency (current, min, max):", cpu_freq.current, cpu_freq.min, cpu_freq.max)
print("CPU Name:", cpu_name)
print("CPU Version:", cpu_version)
print("Host OS:", host_os)
