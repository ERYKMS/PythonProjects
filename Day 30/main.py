
try:
    file=open("a_file.txt")
    a_dict={"key":"value"}
    print(a_dict["not_found_key"])
except FileNotFoundError:
    file=open("a_file.txt","w")
    file.write("Something")
except KeyError as error_massege:
    print(f"the key {error_massege} does not exit")