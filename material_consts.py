# For constants
from python_shogi.shogi import Consts 

''' 
On board values based on YSS 7.0
'''
ON_BOARD_VALUES = { 
        Consts.PAWN  : 1.00, Consts.LANCE: 4.30 , Consts.KNIGHT: 4.50,
        Consts.SILVER: 6.40, Consts.GOLD : 6.90 , 
        Consts.BISHOP: 8.90, Consts.ROOK : 10.40,

        # Promoted Pieces
        # Note -- promoted gold does not exist.

        Consts.PROM_PAWN  : 4.20 , Consts.PROM_LANCE: 6.30, 
        Consts.PROM_KNIGHT: 6.40 , 
        Consts.PROM_SILVER: 6.70 , 
        Consts.PROM_BISHOP: 11.50, Consts.PROM_ROOK: 13.00
        }

''' 
In hand values based on YSS 7.0
''' 
IN_HAND_VALUES = {
         Consts.PAWN  : 1.15 , Consts.LANCE: 4.80 , Consts.KNIGHT: 5.10,   
         Consts.SILVER: 7.20 , Consts.GOLD : 7.80 , 
         Consts.BISHOP: 11.10, Consts.ROOK : 12.70,

         # Add Promoted Pieces to hand as well
         # For some reason add_piece_into_hand allows promoted pieces to be 
         # added, even though they can only be placed back as their unpromoted 
         # versions.
         Consts.PROM_PAWN  : 1.15 , Consts.PROM_LANCE: 4.80 , 
         Consts.PROM_KNIGHT: 5.10 ,   
         Consts.PROM_SILVER: 7.20 , 
         Consts.PROM_BISHOP: 11.10, Consts.PROM_ROOK : 12.70,
         }





