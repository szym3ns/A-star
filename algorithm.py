from node import Node

def algorithm(startPoint, goalPoint, map, allSquares = False):
    openList = []
    closedList = []
    road = []
    childrens = []  
    nearSquares = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    actualNode = Node(startPoint, None)
    goalNode = Node(goalPoint, None)

    openList.append(actualNode)

    while openList:
        actualNode = openList[0]

        for tmpNode in openList:
            if tmpNode.f < actualNode.f:
                actualNode = tmpNode

        openList.remove(actualNode)
        closedList.append(actualNode)

        if actualNode == goalNode:
            tmpNode = actualNode

            while tmpNode is not None:
                road.append(tmpNode.position)
                tmpNode = tmpNode.parent
            return road
    
        childrens = checkChildrens(actualNode, childrens, nearSquares, map)

        for child in childrens:
            for nodeFromClosedList in closedList:
                if (nodeFromClosedList == child):
                    continue
            
            child.g = actualNode.g + 1
            child.h = ((child.position[0] - goalNode.position[0]) ** 2) + ((child.position[1] - goalNode.position[1]) ** 2)
            child.f = child.g + child.h 

            for nodeFromOpenList in openList:
                if (nodeFromOpenList == child and
                    child.g > nodeFromOpenList.g):
                    continue
            
            openList.append(child)

def checkChildrens(actualNode, childrens, nearSquares, map):
    childrens.clear()
    for nearSquare in nearSquares:
        nearSquarePosition = (actualNode.position[0] + nearSquare[0], 
                              actualNode.position[1] + nearSquare[1])
            
        if ((nearSquarePosition[0] < 0 or nearSquarePosition[0] > (len(map) - 1)) or 
            (nearSquarePosition[1] < 0 or nearSquarePosition[1] > (len(map[0]) - 1))):
            continue

        if (map[nearSquarePosition[0]][nearSquarePosition[1]] != 0):
            continue

        tmpNode = Node(nearSquarePosition, actualNode)
        childrens.append(tmpNode)
    return childrens

'''
założenie co do sprawdzania pól: pola z 4 kierunków (jedną kratkę odległości od pola A) - góra, dół, lewo, prawo

openList - 	lista, do której dodajemy pola mogące być ścieżką (ale nie muszą). 
			Generalnie lista z polami do sprawdzenia.
			Pola, które dodajemy to pola z założenia
			
closedList - lista, do której dodajemy pola, które zostały już sprawdzone i
			 nie będą musiały być sprawdzane ponownie.
			 
path - lista, która jest ścieżką

1. 	Zaczynamy w pozycji startowej (np. (0,1)) i dodajemy Node z pozycją startową do openList.

2. 	Dopóki openList nie jest pusta:

	2.1	Inicjalizujemy aktualnego Node, w którym jesteśmy, pierwszym elementem openList.
	
		Następnie w openList szukamy Node, który ma najmniejszą wartość F - czyli 
		w warunku odnosimy się do aktualnego Node, w którym jesteśmy.
		Jeśli znaleźliśmy to dla aktualnego Node przypisujemy Node z listy.
	
	2.2 Usuwamy aktualne pole, w którym jesteśmy, z openList i dodajemy je do closedList.

	2.3 Sprawdzamy czy aktualny Node, w którym jesteśmy jest Nodem końcowym,
		jeśli jest to tworzymy tymczasowego Node któremu przypisujemy aktualnego Node i
		dopóki tymczasowy Node nie ma wartości None to:
		1. Do listy Path dodajemy pozycję tymczasowego Node.
		2. Do tymczasowego Node przypisujemy parenta tego Node.
		
		Na końcu zwracamy odwróconą ścieżkę.
	
	2.4	Sprawdzamy sąsiadujące pola z aktualnym Node, w którym się znajdujemy.
		Przydatna może być tutaj zmienna z nową pozycją naszego Node
		(to znaczy z pozycją z założeń, z sasiądujących pól).
		Jeśli sąsiadujące pole nie jest ścianą oraz nie wykracza poza mape to
		tworzymy nowego Node i nadajemy mu jako parenta aktualnego Node
		oraz jako pozycję zmienną z nową pozycją.
		Na koniec dodajemy nowo stworzonego Node do tablicy z dziećmi.
		
	2.5 Loopujemy po wszytkich dzieciach w tablicy.
	
		2.5.1	Loopujemy po wszystkich Nodach z closedList.
				Jeśli Node z listy closedList jest taki sam jak dziecko z tablicy to szukamy innego dziecka.
				Jeśli nie jest to inicjalizujemy dla dziecka zmienne F, G i H:
				G = G Noda w którym się znajdujemy + 1
				H = (pozycja X dziecka - pozycja X docelowego Node)^2
					+ (pozycja Y dziecka - pozycja Y docelowego Node)^2
				F = G dziecka + H dziecka
		
		2.5.2	Loopujemy po wszystkich Nodach z openList.
				Jeśli Node z listy openList jest taki sam jak dziecko z tablicy 
				ORAZ G dziecka jest większe niż G Noda z openList to szukamy dalej.
				Jeśli nie jest to dodajemy dziecko do openList.
				
KONIEC
						
'''