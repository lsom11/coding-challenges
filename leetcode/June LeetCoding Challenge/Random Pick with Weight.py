class Solution:
  def __init__(self, w):
    ep = 10e-5
    self.N, summ = len(w), sum(w)
    weights = [elem/summ for elem in w]
    Dic_More, Dic_Less, self.Boxes = {}, {}, []
    
    for i in range(self.N):
      if weights[i] >= 1/self.N:
        Dic_More[i] = weights[i]
      else:
        Dic_Less[i] = weights[i]

    while Dic_More and Dic_Less:
      t_1 = next(iter(Dic_More))
      t_2 = next(iter(Dic_Less))
      self.Boxes.append([t_2,t_1,Dic_Less[t_2]*self.N])

      Dic_More[t_1] -= (1/self.N - Dic_Less[t_2])
      if Dic_More[t_1] < 1/self.N - ep:
        Dic_Less[t_1] = Dic_More[t_1]
        Dic_More.pop(t_1)
      Dic_Less.pop(t_2)
    
    for key in Dic_More: self.Boxes.append([key])

  def pickIndex(self):
    r = random.uniform(0, 1)
    Box_num = int(r*self.N)
    if len(self.Boxes[Box_num]) == 1:
      return self.Boxes[Box_num][0]
    else:
      q = random.uniform(0, 1)
      if q < self.Boxes[Box_num][2]:
        return self.Boxes[Box_num][0]
      else:
        return self.Boxes[Box_num][1]