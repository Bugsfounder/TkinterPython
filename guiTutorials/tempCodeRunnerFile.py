   if file == None:
            file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if file=="":
                file = None
            else:
                f = open(file, 'w')
                f.write(userTextResult.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + " - Manisha")
                print("File Saved")
        else:
            f = open(file, 'w')
            f.write(userTextResult.get(1.0, END))
            f.close()