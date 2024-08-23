"""
What is list in python?
=====================================

List - mutable, ordered, duplicate values are allowed, indexing, slicing.

syntax:
list_name = [item1, item2, item3, ...]
empty_list = []
list_name = list()

"""

# items = []
# print(type(items))
# print(len(items))

# Accessing a list elements or whole list

# nums = [1,2,3,4,5]
# print(nums) # [1, 2, 3, 4, 5]

# indexing (-/+)
# print(nums[0]) # 1
# print(nums[-1]) # 5
# print(nums[-2]) # 4

# slicing (-/+)
# print(nums[1:3]) # [2, 3]
# print(nums[1:]) # [2, 3, 4, 5]
# print(nums[:3]) # [1, 2, 3]
# print(nums[:]) # [1, 2, 3, 4, 5]

# concat two or more list
"""
mummy=['milk','banana','potato']
sister=['chocolte','ice-cream']
aunty=['onion','carote','milk']

total_list=mummy+sister+aunty
print(total_list)
"""

# mix_list=[1,2,3,4,"asddasd",35+85j]
# print(mix_list)

# list=list()
# print(dir(list))

"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

"""
1) append:- સૂચિ [1, 2, 3] ના અંતે 4 ઉમેરે છે, જેને પરિણામે [1, 2, 3, 4] બની જાય છે.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # આઉટપુટ: [1, 2, 3, 4]

2) clear() મેટોડ સૂચિમાંના બધા તત્વોને દૂર કરે છે, જેથી સૂચિ ખાલી થાય છે.

my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)  # આઉટપુટ: []

3) copy() મેટોડ સૂચિની પૃથક નકલ બનાવે છે, એટલે કે, મૂળ સૂચિમાં ફેરફાર કરવાથી નકલ પર અસર ન પડે.

my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # આઉટપુટ: [1, 2, 3]

4) count(x) મેટોડ સૂચિમાં x ના તમામ occurrences (ઉપસ્થિતિઓ) ને ગણવે છે.

my_list = [1, 2, 2, 3, 2, 4]
count = my_list.count(2)
print(count)  # આઉટપુટ: 3


5) extend() મેટોડ નવી સૂચિ [4, 5] ના તત્વોને મૂળ સૂચિમાં ઉમેરે છે, જેથી [1, 2, 3] ને [1, 2, 3, 4, 5] માં ફેરવે છે.

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # આઉટપુટ: [1, 2, 3, 4, 5]

6) index(x[, start[, end]])
ઉદ્દેશ: સૂચિમાં તત્વ x ની પ્રથમ occurrences નું સૂચકાંક (index) આપે છે. વિકલ્પરૂપે, તમે શોધને start અને end તરીકે આપેલી મર્યાદાઓમાં કરી શકો છો.

સિyntax: list.index(x[, start[, end]])

my_list = [10, 20, 30, 40, 30]
index = my_list.index(30)
print(index)  # આઉટપુટ: 2

7) insert(i, x)
ઉદ્દેશ: સૂચિમાં વિશિષ્ટ સૂચકાંક i પર તત્વ x નાં ઉમેરવામાં મદદ કરે છે.

સિyntax: list.insert(i, x)

ઉદાહરણ:
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # આઉટપુટ: [1, 4, 2, 3]

વિશેષતા:

i એ તે સૂચકાંક છે જ્યાં તમારે x ઉમેરવું છે.
જો i સૂચિની લંબાઈથી વધુ છે, તો x સૂચિના અંતે ઉમેરાય છે.
જો i નકારાત્મક હોય, તો તે સૂચિની છેલ્લેથી ગણવામાં આવે છે (જેમ કે, -1 છેલ્લું પોઝીશન).

ઉદાહરણ સાથે નકારાત્મક સૂચકાંક:
my_list = [1, 2, 3]
my_list.insert(-1, 4)
print(my_list)  # આઉટપુટ: [1, 2, 4, 3] (4 છેલ્લા પોઝીશનથી પહેલા આવે છે)

8) pop([i])
ઉદ્દેશ: સૂચિમાંથી સૂચકાંક i પરનું તત્વ દૂર કરીને તેને પરત આપે છે. જો i નિર્દિષ્ટ નથી, તો અંતિમ તત્વ દૂર કરે છે.

સિyntax: list.pop([i])

ઉદાહરણ:
my_list = [1, 2, 3, 4]
item = my_list.pop()
print(item)        # આઉટપુટ: 4 (અંતિમ તત્વ દૂર થાય છે)
print(my_list)    # આઉટપુટ: [1, 2, 3]

વિશેષતા:

i પેરામીટર optional છે. જો i આપવું હોય તો તે સૂચકાંક તરીકે કાર્ય કરે છે.
જો આપેલા સૂચકાંક i સીમામાંથી બહાર હોય તો IndexError ઊઠે છે.

ઉદાહરણ સાથે સૂચકાંક:
my_list = [10, 20, 30]
item = my_list.pop(1)
print(item)       # આઉટપુટ: 20 (સૂચકાંક 1 પરનું તત્વ દૂર થાય છે)
print(my_list)   # આઉટપુટ: [10, 30]

ઉદાહરણ સાથે મર્યાદા:
my_list = [1, 2, 3]
item = my_list.pop(5)  # IndexError: pop index out of range

9) remove(2) સૂચિમાં 2 ના પહેલા occurrences ને દૂર કરે છે

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # આઉટપુટ: [1, 3, 2]

10) reverse() મેટોડ સૂચિમાંના તત્વોને સીધા ક્રમમાં ફેરવે છે, છેલ્લું તત્વ પહેલું બનશે અને પહેલું તત્વ છેલ્લું બનશે.

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # આઉટપુટ: [3, 2, 1]

11) key: કસ્ટમ સોર્ટ માટેનો ફંક્શન (optional).
reverse: જો True, તો ઘટાડતા ક્રમમાં સૉર્ટ કરે છે

my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # આઉટપુટ: [1, 2, 3]


"""

