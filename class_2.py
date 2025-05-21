class counting:
    n=0


    def cnt(self):
        self.n = self.n + 1
        print("counted", self.n)

c = counting()

c.cnt()
c.cnt()  # counting.cnt(c)