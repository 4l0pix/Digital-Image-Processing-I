# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 23:10:39 2025

@author: akoukosias
"""
#####################################
import cv2
import numpy as np
import matplotlib.pyplot as plt
#####################################


def display_image(title, image):
    #vasiki sinartisi gia tin emfanisi tis eikonas
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def negative_image(image):
    #dhmiourgia kai provoli tis arnitikis eikonas
    negative = 255 - image #meso kiriolektika antistrofis tis timis tou pixel
    display_image("Negative Image", negative)
    return negative


def apply_average_filter(image, filter_type):
    #efarmogi filtrou mesou orou analoga me thn epilogi tou xristi
    if filter_type == "soft":
        size = 3
    elif filter_type == "medium":
        size = 9
    elif filter_type == "hard":
        size = 15
    else:
        raise ValueError("Lathos typos filtrou. Epilekste 'soft', 'medium', i 'hard'.")
    
    #dimiurgiatou kernel
    kernel = np.ones((size, size), np.float32) / (size * size)
    
    #efarmogh filtrou
    blurred = cv2.filter2D(image, -1, kernel)
    display_image(f"Tholwmeni eikona ({filter_type}, {size}x{size})", blurred)
    return blurred

def sharpen_image(image):
    """oxinsi eikonas me Laplacian"""
    #dimiourgia tou kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    
    #efarmogi tou filtrou oksinsis
    sharpened = cv2.filter2D(image, -1, kernel)
    display_image("Eikona meta tin oksinsi", sharpened)
    return sharpened

def plot_histogram(image):
    plt.style.use('dark_background')
    fig = plt.figure(facecolor='#121212')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#1a1a1a')  
    ax.spines['bottom'].set_color('#6a5acd')  #Slate blue
    ax.spines['top'].set_color('#6a5acd') 
    ax.spines['right'].set_color('#6a5acd')
    ax.spines['left'].set_color('#6a5acd')
    ax.tick_params(axis='x', colors='#9370db')  #Medium purple
    ax.tick_params(axis='y', colors='#9370db')
    
    n, bins, patches = ax.hist(image.ravel(), 256, [0, 256], 
                             color='#483d8b',  #Dark slate blue
                             edgecolor='#9370db',  #Medium purple
                             linewidth=0.5)
    
    #gradient for bars
    for i, patch in enumerate(patches):
        #from blue to purple
        r = 0.3 + 0.7 * (i/256)
        g = 0.2 + 0.3 * (i/256)
        b = 0.7 + 0.3 * (i/256)
        patch.set_facecolor((r, g, b, 0.7))
    
    ax.set_title("Image Histogram", 
                color='#b19cd9',  #light purple
                pad=20, 
                fontsize=12, 
                fontweight='bold')
    ax.set_xlabel("Pixel Value", 
                 color='#b19cd9',
                 labelpad=10)
    ax.set_ylabel("Frequency", 
                 color='#b19cd9',
                 labelpad=10)
    
    #grid lines
    ax.grid(True, 
           color='#4b0082',  #indigo
           linestyle='--', 
           linewidth=0.5, 
           alpha=0.3)
    
    #tight layout
    plt.tight_layout()
    plt.show()

def histogram_matching(input_img, reference_img):
    input_flat = input_img.flatten()
    reference_flat = reference_img.flatten()
    
    hist_input, _ = np.histogram(input_flat, bins=256, range=[0,256])
    hist_ref, _ = np.histogram(reference_flat, bins=256, range=[0,256])
    
    cdf_input = hist_input.cumsum()
    cdf_ref = hist_ref.cumsum()
    cdf_input = (cdf_input - cdf_input.min()) * 255 / (cdf_input.max() - cdf_input.min())
    cdf_ref = (cdf_ref - cdf_ref.min()) * 255 / (cdf_ref.max() - cdf_ref.min())
    
    lookup_table = np.zeros(256)
    lookup_val = 0
    for i in range(256):
        while lookup_val < 255 and cdf_input[i] > cdf_ref[lookup_val]:
            lookup_val += 1
        lookup_table[i] = lookup_val
    
    matched = cv2.LUT(input_img, lookup_table)
    
    display_image("Istogramma eikonas", matched)
    return matched

def main():
    image_path = input("Dose to path tis grayscale eikonas: ")
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if original_image is None:
        print("Lathos: Den mporesa na fortoso tin eikona.")
        return
    
    while True:
        print("\nMenu:")
        print("1. Emfanise arnitiki eikona")
        print("2. Efarmogi filtrou mesou orou")
        print("3. Oxinsi eikonas me Laplacian")
        print("4. Emfanisi istogrammatos")
        print("5. Antistixisi istogrammaton (Part II)")
        print("6. Eksodos")
        
        choice = input("Dose tin epilogi sou (1-6): ")
        
        if choice == "1":
            negative_image(original_image.copy())
        elif choice == "2":
            filter_type = input("Dose ton typo tou filtrou (soft/medium/hard): ").lower()
            try:
                apply_average_filter(original_image.copy(), filter_type)
            except ValueError as e:
                print(e)
        elif choice == "3":
            sharpen_image(original_image.copy())
        elif choice == "4":
            plot_histogram(original_image.copy())
        elif choice == "5":
            print("\nEpiloges anaforas:")
            print("1. Arxiki eikona")
            print("2. Blurred eikona")
            print("3. Oxismeni eikona")
            ref_choice = input("Epilekse eikona anaforas (1-3): ")
            
            reference = None
            if ref_choice == "1":
                reference = original_image.copy()
            elif ref_choice == "2":
                filter_type = input("Dose ton typo tou filtrou gia tin anafora (soft/medium/hard): ").lower()
                try:
                    reference = apply_average_filter(original_image.copy(), filter_type)
                    cv2.destroyAllWindows()
                except ValueError as e:
                    print(e)
                    continue
            elif ref_choice == "3":
                reference = sharpen_image(original_image.copy())
                cv2.destroyAllWindows()
            else:
                print("Lathos epilogi")
                continue
            
            print("\nEpiloges eisodou:")
            print("1. Blurred eikona")
            print("2. Sharpened eikona")
            input_choice = input("Epilekse eikona eisodou (1-2): ")
            
            input_img = None
            if input_choice == "1":
                filter_type = input("Dose ton typo tou filtrou gia tin eisodo (soft/medium/hard): ").lower()
                try:
                    input_img = apply_average_filter(original_image.copy(), filter_type)
                    cv2.destroyAllWindows()
                except ValueError as e:
                    print(e)
                    continue
            elif input_choice == "2":
                input_img = sharpen_image(original_image.copy())
                cv2.destroyAllWindows()
            else:
                print("Lathos epilogi")
                continue
            
            matched = histogram_matching(input_img, reference)
            
            plt.figure(figsize=(12, 6))
            
            plt.subplot(1, 3, 1)
            plt.hist(input_img.ravel(), 256, [0, 256])
            plt.title("Istogramma Eisodou")
            
            plt.subplot(1, 3, 2)
            plt.hist(reference.ravel(), 256, [0, 256])
            plt.title("Istogramma Anaforas")
            
            plt.subplot(1, 3, 3)
            plt.hist(matched.ravel(), 256, [0, 256])
            plt.title("Antistixismeno Istogramma")
            
            plt.tight_layout()
            plt.show()
        elif choice == "6":
            break
        else:
            print("Lathos epilogi. Dokimase ksana.")


#ektelesi script
if __name__ == "__main__":
    main()