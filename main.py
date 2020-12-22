#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from db_management.db_manager import DatabaseManager


if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.create_database()