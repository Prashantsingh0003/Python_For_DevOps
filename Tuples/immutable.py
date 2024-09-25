my_tuple = ("Python", "DevOps", "Docker")
try:
    my_tuple[1] = "Kubernetes"  
except TypeError as e:
    print("Error:", e)