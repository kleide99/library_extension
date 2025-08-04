# -*- coding: utf-8 -*-

from odoo import models,fields,api


class LibraryBook(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.book.category"
    _description = "Book"
    _order = "name"

    ###################
    # Default methods #
    ###################
    name = fields.Char(string="Name",
                       Required= True,
                       Unique= True)
    category_id = fields.Many2many(string="Category")

    ######################
    # Fields declaration #
    ######################

    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################

    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
