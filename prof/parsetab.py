
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "CIRC COLOR DO DOTS ENDFOR FOR IN INT LINE LOAD NEW POINT POLYLINE RAND RECT RECTFILL SAVE STR VAR  program  :   command    program  :  program command    command  :  NEW size color ';'    command  :  LOAD STR ';'    command  :  SAVE STR ';'    command  :  COLOR color ';'    command  :  POINT point color ';'\n                      | POINT point ';'   command  :  LINE  point point color ';'\n                      | LINE point point ';'    command  :  RECT  point point color ';'\n                      |  RECT  point size color ';'\n                      |  RECT  point point ';'\n                      |  RECT  point size ';'        command  :  RECTFILL  point point color ';'\n                      |  RECTFILL  point size color ';'\n                      |  RECTFILL  point point ';'\n                      |  RECTFILL  point size ';'        command  :  CIRC  point INT color ';'\n                      | CIRC point INT ';'    command  :  POLYLINE points color ';'\n                      |  POLYLINE points ';'    command  :  FOR VAR IN '[' value DOTS value ']' DO program ENDFOR ';'    command  :   VAR '=' value ';'   points  :  point    points  :  points point    point : value ',' value   size : value 'x' value   color :  value ':' value ':' value    value  :   INT\n                    |   VAR\n                    |   RAND value "
    
_lr_action_items = {'NEW':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[3,3,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,3,3,-23,]),'LOAD':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[4,4,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,4,4,-23,]),'SAVE':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[5,5,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,5,5,-23,]),'COLOR':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[6,6,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,6,6,-23,]),'POINT':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[7,7,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,7,7,-23,]),'LINE':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[8,8,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,8,8,-23,]),'RECT':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[9,9,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,9,9,-23,]),'RECTFILL':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[10,10,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,10,10,-23,]),'CIRC':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[11,11,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,11,11,-23,]),'POLYLINE':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[12,12,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,12,12,-23,]),'FOR':([0,1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,90,91,93,],[13,13,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,13,13,-23,]),'VAR':([0,1,2,3,6,7,8,9,10,11,12,13,15,16,18,19,20,25,27,28,29,31,32,34,36,37,38,39,40,41,43,44,45,46,47,49,50,51,53,54,58,59,61,62,64,66,68,70,72,74,75,76,77,78,79,80,81,82,83,84,87,90,91,93,],[14,14,-1,19,19,19,19,19,19,19,19,33,-2,19,-30,-31,19,19,19,19,19,19,-25,19,19,-32,-4,-5,-6,19,-8,19,19,19,19,19,19,19,-22,-26,-3,-28,-7,-27,-10,-13,-14,-17,-18,-20,-21,19,-24,19,-9,-11,-12,-15,-16,-19,19,14,14,-23,]),'$end':([1,2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,93,],[0,-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,-23,]),'ENDFOR':([2,15,38,39,40,43,53,58,61,64,66,68,70,72,74,75,77,79,80,81,82,83,84,91,93,],[-1,-2,-4,-5,-6,-8,-22,-3,-7,-10,-13,-14,-17,-18,-20,-21,-24,-9,-11,-12,-15,-16,-19,92,-23,]),'INT':([3,6,7,8,9,10,11,12,16,18,19,20,25,27,28,29,30,31,32,34,36,37,41,44,45,46,47,49,50,51,54,59,62,76,78,87,],[18,18,18,18,18,18,18,18,18,-30,-31,18,18,18,18,18,51,18,-25,18,18,-32,18,18,18,18,18,18,18,18,-26,-28,-27,18,18,18,]),'RAND':([3,6,7,8,9,10,11,12,16,18,19,20,25,27,28,29,31,32,34,36,37,41,44,45,46,47,49,50,51,54,59,62,76,78,87,],[20,20,20,20,20,20,20,20,20,-30,-31,20,20,20,20,20,20,-25,20,20,-32,20,20,20,20,20,20,20,20,-26,-28,-27,20,20,20,]),'STR':([4,5,],[21,22,]),'=':([14,],[34,]),'x':([17,18,19,37,48,],[36,-30,-31,-32,36,]),':':([18,19,24,37,55,60,],[-30,-31,41,-32,41,78,]),',':([18,19,26,37,48,55,],[-30,-31,44,-32,44,44,]),';':([18,19,21,22,23,25,31,32,35,37,42,45,46,47,49,50,51,52,54,57,59,62,63,65,67,69,71,73,86,92,],[-30,-31,38,39,40,43,53,-25,58,-32,61,64,66,68,70,72,74,75,-26,77,-28,-27,79,80,81,82,83,84,-29,93,]),'DOTS':([18,19,37,85,],[-30,-31,-32,87,]),']':([18,19,37,88,],[-30,-31,-32,89,]),'IN':([33,],[56,]),'[':([56,],[76,]),'DO':([89,],[90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,90,],[1,91,]),'command':([0,1,90,91,],[2,15,2,15,]),'size':([3,28,29,],[16,47,50,]),'value':([3,6,7,8,9,10,11,12,16,20,25,27,28,29,31,34,36,41,44,45,46,47,49,50,51,76,78,87,],[17,24,26,26,26,26,26,26,24,37,24,26,48,48,55,57,59,60,62,24,24,24,24,24,24,85,86,88,]),'color':([6,16,25,31,45,46,47,49,50,51,],[23,35,42,52,63,65,67,69,71,73,]),'point':([7,8,9,10,11,12,27,28,29,31,],[25,27,28,29,30,32,45,46,49,54,]),'points':([12,],[31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> command','program',1,'p_program0','Parser.py',57),
  ('program -> program command','program',2,'p_program1','Parser.py',61),
  ('command -> NEW size color ;','command',4,'p_command0','Parser.py',67),
  ('command -> LOAD STR ;','command',3,'p_command1','Parser.py',71),
  ('command -> SAVE STR ;','command',3,'p_command2','Parser.py',74),
  ('command -> COLOR color ;','command',3,'p_command3','Parser.py',78),
  ('command -> POINT point color ;','command',4,'p_command4','Parser.py',81),
  ('command -> POINT point ;','command',3,'p_command4','Parser.py',82),
  ('command -> LINE point point color ;','command',5,'p_command5','Parser.py',86),
  ('command -> LINE point point ;','command',4,'p_command5','Parser.py',87),
  ('command -> RECT point point color ;','command',5,'p_command6','Parser.py',90),
  ('command -> RECT point size color ;','command',5,'p_command6','Parser.py',91),
  ('command -> RECT point point ;','command',4,'p_command6','Parser.py',92),
  ('command -> RECT point size ;','command',4,'p_command6','Parser.py',93),
  ('command -> RECTFILL point point color ;','command',5,'p_command7','Parser.py',107),
  ('command -> RECTFILL point size color ;','command',5,'p_command7','Parser.py',108),
  ('command -> RECTFILL point point ;','command',4,'p_command7','Parser.py',109),
  ('command -> RECTFILL point size ;','command',4,'p_command7','Parser.py',110),
  ('command -> CIRC point INT color ;','command',5,'p_command8','Parser.py',113),
  ('command -> CIRC point INT ;','command',4,'p_command8','Parser.py',114),
  ('command -> POLYLINE points color ;','command',4,'p_command9','Parser.py',117),
  ('command -> POLYLINE points ;','command',3,'p_command9','Parser.py',118),
  ('command -> FOR VAR IN [ value DOTS value ] DO program ENDFOR ;','command',12,'p_command_for','Parser.py',125),
  ('command -> VAR = value ;','command',4,'p_command_10','Parser.py',134),
  ('points -> point','points',1,'p_points0','Parser.py',139),
  ('points -> points point','points',2,'p_points1','Parser.py',143),
  ('point -> value , value','point',3,'p_point','Parser.py',148),
  ('size -> value x value','size',3,'p_size','Parser.py',152),
  ('color -> value : value : value','color',5,'p_color','Parser.py',156),
  ('value -> INT','value',1,'p_value','Parser.py',160),
  ('value -> VAR','value',1,'p_value','Parser.py',161),
  ('value -> RAND value','value',2,'p_value','Parser.py',162),
]