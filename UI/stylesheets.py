from enum import Enum

class GridButtonType(Enum):
    NORMAL = 0
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_RIGHT = 3
    BOTTOM_LEFT = 4


class GridButtonStylesheets():
    def __init__(self):
        
        self.normal_spritesheet = """
        QPushButton {
            background-color: #DB6A23;
            color: white;
            border: 2px solid #DB6A23;
            border-radius: 8px;
            padding: 0px;
            font: bold 12px;
        }
        
        QPushButton:hover {
            background-color: #EE7224;
            border: 2px solid #EE7224;
            color: white;
        }
        
        QPushButton:pressed {
            background-color: #C54C00;
            border: 2px solid #C54C00;
            color: white;
        }
        """


        self.label_style_sheet = """
        QLabel 
        {
            background-color: #00000000;
            color: #FFFFFF;
            font: bold 24px;
        }

        """

        self.simulated_label_style_sheet = """
        QLabel 
        {
            background-color: #00000000;
            color: #DDDDDDDD;
            font: bold 24px;
        }

        """

    def getStylesheetForType(self, round_type):
        if round_type == GridButtonType.NORMAL:
            return self.normal_spritesheet
        if round_type == GridButtonType.TOP_LEFT:
            return self.top_left_spritesheet
        if round_type == GridButtonType.TOP_RIGHT:
            return self.top_right_spritesheet
        if round_type == GridButtonType.BOTTOM_RIGHT:
            return self.bottom_right_spritesheet
        if round_type == GridButtonType.BOTTOM_LEFT:
            return self.bottom_left_spritesheet
        
    def getLabelStylesheet(self):
        return self.label_style_sheet
    
    def getSimulatedLabelStylesheet(self):
        return self.simulated_label_style_sheet
    
    
class ProblemCreationSpriteSheets():
    def __init__(self):
        self.text_edit_style_sheet = """
        QTextEdit {
            background-color: #EEEEEE; 
            border: 2px solid #DB6A23; 
            border-radius: 4px; 
            padding: 2px; 
            font: 16px; 
        }

        QTextEdit:hover {
            border: 2px solid #FFA500; 
        }

        QTextEdit:focus {
            border: 2px solid #FFA500; 
        }
        """

        self.problem_manager_button = """        
        QPushButton {
                background-color: #DB6A23;
                color: white;
                border: 2px solid #DB6A23;
                border-radius: 8px;
                padding: 0px;
                font: bold 24px;
            }
            
            QPushButton:hover {
                background-color: #EE7224;
                border: 2px solid #EE7224;
                color: white;
            }
            
            QPushButton:pressed {
                background-color: #C54C00;
                border: 2px solid #C54C00;
                color: white;
            }
            """

        self.scroller_style_sheet = """
                QScrollArea {
                    border: none;
                }

                QScrollBar {
                    background: rgba(240,230,205,255);;
                    border-radius: 5px;
                }

                QScrollBar:horizontal {
                    height: 13px;
                }

                QScrollBar:vertical {
                    width: 13px;
                }

                QScrollBar::handle {
                    background: #DB6A23;
                    border-radius: 5px;
                }

                QScrollBar::handle:horizontal {
                    height: 25px;
                    min-width: 10px;
                }

                QScrollBar::handle:vertical {
                    width: 25px;
                    min-height: 10px;
                }

                QScrollBar::add-line {
                    border: none;
                    background: none;
                }

                QScrollBar::sub-line {
                    border: none;
                    background: none;
                }
                """
        
        self.combobox_style_sheet = """
        QComboBox {
            background: #EEEEEE;
            border: 2px solid #DB6A23; 
            border-radius: 4px; 
            font: 16px; 
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px; 
            border-left: 2px solid #DB6A23; 
            border-top-right-radius: 8px; 
            border-bottom-right-radius: 8px;
        }

        QComboBox:hover {
            border: 2px solid #EE7224; 
        }
        """

    def getTextEditStylesheet(self):
        return self.text_edit_style_sheet

    def getProblemManagerButton(self):
        return self.problem_manager_button
    
    def getScrollerStylesheet(self):
        return self.scroller_style_sheet
    
    def getComboboxStylesheet(self):
        return self.combobox_style_sheet
    
