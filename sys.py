import sys
import cowsay

def main():
    if len(sys.argv) < 2:
        ## affichie un message 
        ## print("Too few arguments")
        sys.exit("Too few Arguments")
    
    for arg in sys.argv:
        print(f"{arg}")

    #use slices
    print("Print using slices:")
    for arg in sys.argv[1:]:
        print(f"arg : {arg}")

    #sys.version
    print(sys.version)
    print(sys.platform)
    
    #use the package cowsay by the package cowsay installed by pip

    cowsay.cow("MOOOOOOOO")
    
    my_fish = "r'''"

    cowsay.trex("Hi iam a fish")


main()
