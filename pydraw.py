# saruav
import pygame
import random
import time

pygame.font.init()
startTime = time.time()

screen = pygame.display.set_mode((1200, 590))
pygame.display.set_caption("SORTING VISUALISER")

Running = True
fill_col = (20, 20, 20)

# sorting algorithms


# heapsort
def heapSort(array):
    n = len(array)
    for i in range(n//2-1, -1, -1):
        pygame.event.pump()
        heapify(array, i, n)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        arr_clr[i] = clr[1]
        refill()
        heapify(array, 0, i)


def heapify(array, root, size):
    left = root * 2 + 1
    right = root * 2 + 2
    largest = root
    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != root:
        arr_clr[largest] = clr[2]
        arr_clr[root] = clr[2]
        array[largest], \
            array[root] = array[root], \
            array[largest]
        refill()
        arr_clr[largest] = clr[0]
        arr_clr[root] = clr[0]
        heapify(array, largest, size)
        refill()


# Bubble Sort


def bubbleSort(array):
    pygame.event.pump()
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            arr_clr[j] = clr[2]
            arr_clr[j+1] = clr[2]
            if array[j] > array[j+1]:
                arr_clr[j] = clr[3]
                arr_clr[j+1] = clr[3]
                array[j], array[j+1] = array[j+1], array[j]
                refill()
                arr_clr[j] = clr[0]
                arr_clr[j+1] = clr[0]
            else:
                refill()
                arr_clr[j] = clr[0]
                arr_clr[j+1] = clr[0]
        arr_clr[len(array)-i-1] = clr[1]
        refill()


# Selection Sort


def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        arr_clr[i] = clr[2]
        refill()
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                arr_clr[min_idx] = clr[0]
                min_idx = j
                arr_clr[min_idx] = clr[3]
                refill()
            else:
                arr_clr[j] = clr[2]
                refill()
                arr_clr[j] = clr[0]
        arr_clr[min_idx] = clr[2]
        array[i], array[min_idx] = array[min_idx], array[i]
        arr_clr[i] = clr[1]
        refill()
        arr_clr[min_idx] = clr[0]

# Insertion Sort


def insertionSort(array):
    for i in range(len(array)):
        cursor = array[i]
        arr_clr[i] = clr[2]
        refill()
        idx = i
        while idx > 0 and array[idx-1] > cursor:
            arr_clr[idx] = clr[2]
            arr_clr[idx-1] = clr[2]
            refill()
            array[idx] = array[idx-1]
            arr_clr[idx] = clr[1]
            arr_clr[idx-1] = clr[1]
            idx -= 1

        array[idx] = cursor
        arr_clr[idx] = clr[1]
        if(idx != i):
            arr_clr[i] = clr[1]
        refill()

# Quick Sort


def partition(arr, low, high):
    i = (low-1)
    arr_clr[high] = clr[3]
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i+1
            arr_clr[i] = clr[2]
            arr_clr[j] = clr[2]
            arr[i], arr[j] = arr[j], arr[i]
            refill()
            arr_clr[i] = clr[0]
            arr_clr[j] = clr[0]

    arr_clr[i+1] = clr[3]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    refill()
    arr_clr[high] = clr[0]
    arr_clr[i+1] = clr[0]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        refill()
        quickSort(arr, pi+1, high)
        refill()


def colorSerially(array):
    for i in range(0, len(array)):
        arr_clr[i] = clr[1]
        refill()

# Merge Sort


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
            for var in range(mid, len(myList)):
                arr_clr[var] = clr[2]
            for var in range(0, mid):
                arr_clr[var] = clr[3]
            refill()

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
            for var in range(mid, len(myList)):
                arr_clr[var] = clr[2]
            for var in range(0, mid):
                arr_clr[var] = clr[3]
            refill()

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
            for var in range(mid, len(myList)):
                arr_clr[var] = clr[2]
            for var in range(0, mid):
                arr_clr[var] = clr[3]
            refill()

        for var in range(mid, len(myList)):
            arr_clr[var] = clr[0]
        for var in range(0, mid):
            arr_clr[var] = clr[0]


# variables
delay = 10
txt_clr = (169, 169, 169)
bar_clr = (0, 155, 158)
fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 50)
fnt2 = pygame.font.SysFont("comicsans", 20)
width = 900
length = 550
array = [0]*151
arr_clr = [bar_clr]*151
clr_ind = 0
clr = [(0, 155, 158), (176, 0, 81), (250, 157, 0), (255, 64, 35)]
algo_using = "Algorithm Used : "


def generate_arr():
    for i in range(1, 151):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 100)


def refill():
    screen.fill(fill_col)
    draw()
    pygame.display.update()
    pygame.time.delay(delay)


def draw():
    pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(0, 0, 300, 590))
    pygame.draw.rect(screen, (0, 62, 81), pygame.Rect(300, 0, 900, 40))
    pygame.draw.rect(screen, (64, 64, 64), pygame.Rect(0, 200, 300, 40))
    pygame.draw.rect(screen, (64, 64, 64), pygame.Rect(0, 280, 300, 40))
    pygame.draw.rect(screen, (64, 64, 64), pygame.Rect(0, 360, 300, 40))
    pygame.draw.rect(screen, (0, 62, 81), pygame.Rect(0, 480, 300, 40))
    txt = fnt.render("Press 1 : Quick Sort", 1, txt_clr)
    screen.blit(txt, (50, 210))
    txt = fnt.render("Press 2 : Heap Sort", 1, txt_clr)
    screen.blit(txt, (50, 250))
    txt = fnt.render("Press 3 : Merge Sort", 1, txt_clr)
    screen.blit(txt, (50, 290))
    txt = fnt.render("Press 4 : Bubble Sort", 1, txt_clr)
    screen.blit(txt, (50, 330))
    txt = fnt.render("Press 5 : Insertion Sort", 1, txt_clr)
    screen.blit(txt, (50, 370))
    txt = fnt.render("Press 6 : Selection Sort", 1, txt_clr)
    screen.blit(txt, (50, 410))
    txt = fnt1.render("SORTING", 1, bar_clr)
    screen.blit(txt, (65, 50))
    txt = fnt1.render("VISUALISER", 1, bar_clr)
    screen.blit(txt, (40, 100))
    txt = fnt.render("Press R : generate arr", 1, txt_clr)
    screen.blit(txt, (50, 490))
    txt = fnt2.render("Running Time(sec): " +
                      str(int(time.time() - startTime)), 1, txt_clr)
    screen.blit(txt, (1000, 15))
    txt = fnt.render(algo_using, 1, txt_clr)
    screen.blit(txt, (350, 10))

    element_width = (width-150)//150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100

    # Drawing the array values as lines
    for i in range(1, 151):
        pygame.draw.line(screen, arr_clr[i],
                         (300+boundry_arr * i-3, 590),
                         (300+boundry_arr * i-3, 590-array[i]*boundry_grp),
                         element_width)


generate_arr()

while Running:
    screen.fill(fill_col)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                algo_using = "Algorithm Used :"
                generate_arr()
            if event.key == pygame.K_1:
                algo_using = "Algorithm Used : QuickSort"
                quickSort(array, 0, len(array)-1)
                colorSerially(array)
            if event.key == pygame.K_2:
                algo_using = "Algorithm Used : HeapSort"
                heapSort(array)
            if event.key == pygame.K_3:
                algo_using = "Algorithm Used : MergeSort"
                mergeSort(array)
            if event.key == pygame.K_4:
                algo_using = "Algorithm Used : BubbleSort"
                bubbleSort(array)
            if event.key == pygame.K_5:
                algo_using = "Algorithm Used : InsetrionSort"
                insertionSort(array)
            if event.key == pygame.K_6:
                algo_using = "Algorithm Used : SelectionSort"
                selectionSort(array)

    draw()
    pygame.display.update()

pygame.quit()
