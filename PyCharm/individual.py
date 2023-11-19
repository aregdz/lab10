#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"a", "d", "k", "l", "o", "s"}
    b = {"d", "e", "k", "s", "u", "x"}
    c = {"o", "p", "w"}
    d = {"d", "n", "r", "y", "z"}

    x = (a.difference(b)).union(c.intersection(d))
    print(f"x = {x}")

    da = u.difference(a)
    db = u.difference(b)
    y = (da.intersection(db)).difference(c.union(d))
    print(f"y = {y}")