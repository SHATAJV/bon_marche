#!/usr/bin/env python


# -*- coding: utf-8 -*-
import store
from store import Store


def main():
     store= Store()
     store.store_menu()
     stock(store)

if __name__=="__main__" :
     main()