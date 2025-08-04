# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    ######################
    # Private attributes #
    ######################

    _inherit = "library.book"

    ###################
    # Default methods #
    ###################


    ######################
    # Fields declaration #
    ######################
    author_id = fields.Many2one(
                            string="Author",
                            comodel_name="res.partner",
                            required=True,
                            unique=True)
    category_id = fields.Many2many(
                            string="Category",
                            comodel_name="library.book.category")
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
