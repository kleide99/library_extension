# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBookCategory(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.extension"
    _description = "Book Category"
    _order = "name"

    ###################
    # Default methods #
    ###################
    author_id = fields.Many2one(
                            string="Name",
                            comodel_name="res.partner",
                            required=True,
                            unique=True)
    category_id = fields.Many2many(
                            string="Category",
                            required=True)

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
