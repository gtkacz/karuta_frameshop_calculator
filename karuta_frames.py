import numpy as np, tkinter, customtkinter

def find_frames(positive_bits: list[str]) -> list[str]:
    frames = {
        'Brass': ['Copper', 'Zinc', 2],
        'Fortress': ['Stone', 'Wood', 3],
        'Beachside': ['Flower', 'Quartz', 4],
        'Volcanic': ['Copper', 'Magma', 5],
        'Cherry Blossom': ['Flower', 'Wood', 6],
        'Spirit Flame': ['Bone', 'Wood', 7],
        'Night Crow': ['Bone', 'Zinc', 8],
        'Crystal Mines': ['Quartz', 'Stone', 9],
        'Submarine': ['Iron', 'Uranium', 10],
        'Pirate Voyage': ['Iron', 'Wood', 11],
        'Kominka': ['Essence', 'Wood', 12],
        'Magus': ['Essence', 'Zinc', 13],
        'Magitek': ['Magma', 'Uranium', 14],
        'Snowlands': ['Ice', 'Wood', 15],
        'Ice Cream Sundae': ['Ice', 'Sugar', 16],
        'Dragon Hunt': ['Bone', 'Wool', 17],
        'Patchwork': ['Essence', 'Wool', 18],
        'Venice Carnival': ['Flower', 'Zinc', 19],
        'Robotic': ['Essence', 'Uranium', 20],
        'Frills': ['Quartz', 'Wool', 21],
        'Fuselage': ['Iron', 'Zinc', 22],
        'Rozen': ['Flower', 'Stone', 23],
        'Smithy Forge': ['Magma', 'Stone', 24],
        'Watermelon Juice': ['Leaf', 'Sugar', 25],
        'Faerie Forest': ['Flower', 'Leaf', 26],
        'Autumn View': ['Leaf', 'Stone', 27],
        'Edo Furin': ['Copper', 'Quartz', 28],
        'Barbecue': ['Salt', 'Zinc', 29],
        'Whirlpool': ['Ice', 'Salt', 30],
        'Bubble Bath': ['Ice', 'Wool', 31],
        'Spaceship': ['Uranium', 'Zinc', 32],
        'Wild West': ['Quartz', 'Wood', 33],
        'Archery': ['Copper', 'Wood', 34],
        'Tree Frog': ['Bone', 'Leaf', 35],
        'Scimitar Fight': ['Bone', 'Iron', 36],
        'Bamboo Stalks': ['Leaf', 'Wood', 37],
        'Chocolate Orange': ['Essence', 'Sugar', 38],
        'Tribal Chief': ['Copper', 'Stone', 39],
        'Abandoned Church': ['Leaf', 'Quartz', 40],
        'Long Hair': ['Essence', 'Salt', 41],
        'Water Element': ['Ice', 'Quartz', 42],
        'Carved Stone': ['Clay', 'Stone', 43],
        'Beauty': ['Clay', 'Flower', 44],
        'Carnations': ['Flower', 'Wool', 45],
        'Baroque': ['Clay', 'Copper', 46],
        'Musical Notes': ['Essence', 'Iron', 47],
        "Winner's Podium": ['Iron', 'Stone', 48],
        'Manticore': ['Bone', 'Magma', 49],
        'Tipsy': ['Salt', 'Sugar', 50],
        'Nordic': ['Salt', 'Stone', 51],
        'Shiba Inu': ['Bone', 'Essence', 52],
        'Toy Mecha': ['Ice', 'Uranium', 53],
        'Bubble Tea': ['Ice', 'Leaf', 54],
        'Morning Dew': ['Flower', 'Ice', 55],
        "Nurse's Office": ['Bone', 'Sugar', 56],
        'Honeycomb': ['Sugar', 'Wax', 57],
        'Magical Girl': ['Quartz', 'Sugar', 58],
        'Tetromino': ['Essence', 'Wax', 59],
        'Flying Dragon': ['Bone', 'Oil', 60],
        'Gaming Chair': ['Oil', 'Wool', 61],
        'Tanglung': ['Flower', 'Oil', 62],
        'Pastel Geometry': ['Wax', 'Uranium', 63],
        'Lighthouse Storm': ['Ice', 'Stone', 64],
        'Chopsticks': ['Salt', 'Wood', 65],
        'Haunted Stone': ['Essence', 'Stone', 66],
        'Kawaii Bento': ['Salt', 'Wool', 67],
        'Pocket Pet': ['Bone', 'Clay', 68],
        'Jade Cherrywood': ['Clay', 'Wood', 69],
        'Pharaoh': ['Clay', 'Magma', 70],
        'Shisa': ['Leaf', 'Salt', 71],
        'Butterfly Garden': ['Essence', 'Leaf', 72],
        'Labpunk': ['Oil', 'Quartz', 73],
        "Wizard's Hut": ['Oil', 'Stone', 74],
        'Flame Temple': ['Oil', 'Zinc', 75],
        'Night Ooze': ['Quartz', 'Wax', 76],
        'Prehistoric': ['Bone', 'Zinc', 77],
        'Malice Tree': ['Magma', 'Wood', 78],
        'Bewitched Parchment': ['Essence', 'Oil', 79],
        'Kraken': ['Salt', 'Wax', 80],
        'Reclaimed by Nature': ['Clay', 'Leaf', 81],
        'Cherry Berry': ['Flower', 'Sugar', 82],
        'Seamster': ['Wood', 'Wool', 83],
    }

    possible_frames = {}
    
    for frame_name, frame_bits in frames.items():
        if frame_bits[0] in positive_bits and frame_bits[1] in positive_bits:
            possible_frames[frame_name] = frames[frame_name][2]

    return possible_frames

def main():
    root = tkinter.Tk()
    root.title("Karuta Frames")
    root.geometry("615x185")
    customtkinter.set_appearance_mode("Dark")

    sub_list_count = 5
    
    corner_radius = 25
    text_color = ('#000000', '#000000')
    font = ('Calibri', 14)
    width = 120
    height = 25
    
    positive_bits = []
    all_bits = ['Bone', 'Clay', 'Copper', 'Essence', 'Flower', 'Ice', 'Iron', 'Leaf', 'Magma', 'Oil', 'Quartz', 'Salt', 'Stone', 'Sugar', 'Uranium', 'Wax', 'Wood', 'Wool', 'Zinc']
    bits_var = [tkinter.StringVar() for i in range(len(all_bits))]

    sub_lists = np.array_split(all_bits, sub_list_count)

    customtkinter.CTkLabel(master=root, text='Which bits do you have >2500 of?', width=width, height=height, text_color=text_color, font=font+('bold',)).grid(row=0, column=0, padx=9)
    
    for i, list in enumerate(sub_lists):
        for c, bit in enumerate(list):
            if i != (sub_list_count - 1):
                customtkinter.CTkCheckBox(master=root, text=bit, width=width, height=height, checkbox_width=height//1.5, checkbox_height=height//1.5, corner_radius=corner_radius, text_color=text_color, font=font, hover=True, variable=bits_var[((i+c) + ((len(list) * i) - i))], onvalue=bit, offvalue='').grid(row=i+1, column=c, padx=9)
            else:
                customtkinter.CTkCheckBox(master=root, text=bit, width=width, height=height, checkbox_width=height//1.5, checkbox_height=height//1.5, corner_radius=corner_radius, text_color=text_color, font=font, hover=True, variable=bits_var[(i**2)+c], onvalue=bit, offvalue='').grid(row=i+1, column=c, padx=9)

    # customtkinter.CTkLabel(master=root).grid(row=0, column=c+2)
    
    def button_function():
        nonlocal root

        for bit in bits_var:
            curr_bit = bit.get()
            if curr_bit != '':
                positive_bits.append(curr_bit)
        
        results = find_frames(positive_bits)

        for widget in root.winfo_children():
            widget.destroy()

        customtkinter.CTkLabel(master=root, text='You can buy:', width=width, height=height, text_color=text_color, font=font+('bold',)).grid(row=0, column=0, pady=15)

        for p, (frame_name, frame_index) in enumerate(results.items()):
            customtkinter.CTkLabel(master=root, text=f'{frame_index}. {frame_name} Frame', width=width, height=height, text_color=text_color, font=font).grid(row=p+1, column=0, padx=10)

        root.geometry(f"180x{60 + (len(results) * 25)}")
    
    button = customtkinter.CTkButton(master=root, corner_radius=corner_radius, text='Calculate', command=button_function)
    
    button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
    
    root.mainloop()

if __name__ == "__main__":
    main()
    # print(find_frames(['Iron', 'Oil', 'Uranium', 'Wax', 'Salt', 'Sugar', 'Leaf', 'Stone', 'Clay', 'Essence']))