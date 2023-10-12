def get_formal_name(fruit, default=None):

    fruit_dict = {
            'apple': 'Malus domestica',
            'banana': 'Musa acuminata',
            'orange': 'Citrus × sinensis',
            'strawberry': 'Fragaria × ananassa',
            'grape': 'Vitis vinifera',
            'pineapple': 'Ananas comosus',
            'mango': 'Mangifera indica',
            'blueberry': 'Vaccinium corymbosum',
            'peach': 'Prunus persica',
            'watermelon': 'Citrullus lanatus',
            'cherry': 'Prunus avium',
            'pear': 'Pyrus',
            'plum': 'Prunus domestica',
            'raspberry': 'Rubus idaeus',
            'kiwi': 'Actinidia deliciosa',
            'lemon': 'Citrus limon',
            'avocado': 'Persea americana',
            'pomegranate': 'Punica granatum',
            'cranberry': 'Vaccinium macrocarpon',
            'grapefruit': 'Citrus × paradisi'
        }

    formal_name = fruit_dict.get(fruit, default)
    
    return formal_name