# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBookCategory(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    ###################
    # Default methods #
    ###################
    

    ######################
    # Fields declaration #
    ######################
    author_id = fields.Many2one(
                            string="Name",
                            comodel_name="res.partner",
                            required=True,)
    
    category_id = fields.Many2many(
                            string="Category",
                            required=True)

    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constraints and onchanges #
    ############################

    _sql_constraints = [
        ('unique_author_constraint', 'unique(author_id,), 'An author must be unique.'),]
    _sql_constraints = [
        ('unique_category_constraint', 'unique(category_id,), 'A category must be unique.'),]
        
    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    category_obj = env['library.book.category'].create({
        'name': 'Action',}]
    duplicate_category_obj = env['library.book.category'].create({
        'name': 'Action',}]
    author = env['res.partner'].create({
        'name': 'Michael Jackson',}]
    book = env['library.book']

    ####################
    # Business methods #
    ####################

