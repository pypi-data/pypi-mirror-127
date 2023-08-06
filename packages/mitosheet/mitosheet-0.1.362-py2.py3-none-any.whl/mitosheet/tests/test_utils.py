#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
This file contains helpful functions and classes for testing operations.
"""

import json
from typing import List

import pandas as pd
from mitosheet.mito_widget import MitoWidget, sheet
from mitosheet.transpiler.transpile import transpile
from mitosheet.utils import get_new_id
from mitosheet.api.get_sheet_data import get_sheet_data


class MitoWidgetTestWrapper:
    """
    This class adds some simple wrapper functions onto the MitoWidget 
    to make interacting with it easier for testing purposes.

    It allows you to create just the backend piece of Mito, create columns,
    set formulas, and get values to check the result.
    """

    def __init__(self, mito_widget: MitoWidget):
        self.mito_widget = mito_widget

    @property
    def transpiled_code(self):
        # NOTE: we don't add comments to this testing functionality, so that 
        # we don't have to change tests if we update comments
        return transpile(self.mito_widget.steps_manager, add_comments=False)['code']

    @property
    def dfs(self):
        return self.mito_widget.steps_manager.dfs

    def add_column(self, sheet_index: int, column_header: str, column_header_index=-1):
        """
        Adds a column.
        """

        return self.mito_widget.receive_message(self.mito_widget, {
            'event': 'edit_event',
            'id': get_new_id(),
            'type': 'add_column_edit',
            'step_id': get_new_id(),
            'params': {
                'sheet_index': sheet_index,
                'column_header': column_header,
                'column_header_index': column_header_index
            }
        })
    
    def set_formula(
            self, 
            formula: str, 
            sheet_index: int,
            column_header: str, 
            add_column=False,
        ):
        """
        Sets the given column to have formula, and optionally
        adds the column if it does not already exist.
        """
        if add_column:
            self.add_column(sheet_index, column_header)

        column_id = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            column_header
        )

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'set_column_formula_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_id': column_id,
                    'new_formula': formula,
                }
            }
        )

    def merge_sheets(
            self, 
            how,
            sheet_index_one, 
            merge_key_one, 
            selected_columns_one,
            sheet_index_two, 
            merge_key_two,
            selected_columns_two
        ):

        merge_key_column_id_one = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index_one,
            merge_key_one
        )
        merge_key_column_id_two = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index_two,
            merge_key_two
        )
        selected_column_ids_one = [
            self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(sheet_index_one, column_header)
            for column_header in selected_columns_one
        ]
        selected_column_ids_two = [
            self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(sheet_index_two, column_header)
            for column_header in selected_columns_two
        ]

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'merge_edit',
                'step_id': get_new_id(),
                'params': {
                    'how': how,
                    'sheet_index_one': sheet_index_one,
                    'merge_key_column_id_one': merge_key_column_id_one,
                    'selected_column_ids_one': selected_column_ids_one,
                    'sheet_index_two': sheet_index_two,
                    'merge_key_column_id_two': merge_key_column_id_two,
                    'selected_column_ids_two': selected_column_ids_two
                }
            }
        )

    def pivot_sheet(
            self, 
            sheet_index, 
            pivot_rows,
            pivot_columns,
            values,
            destination_sheet_index=None,
            step_id=None
        ):

        rows_ids = [
            self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(sheet_index, column_header)
            for column_header in pivot_rows
        ]
        columns_ids = [
            self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(sheet_index, column_header)
            for column_header in pivot_columns
        ]
        values_column_ids_map = {
            self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(sheet_index, column_header): value
            for column_header, value in values.items()
        }

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'pivot_edit',
                'step_id': get_new_id() if step_id is None else step_id,
                'params': {
                    'sheet_index': sheet_index,
                    'pivot_rows_column_ids': rows_ids,
                    'pivot_columns_column_ids': columns_ids,
                    'values_column_ids_map': values_column_ids_map,
                    'destination_sheet_index': destination_sheet_index
                }
            }
        )

    def filter(
            self, 
            sheet_index, 
            column_header,
            operator,
            type_,
            condition, 
            value
        ):

        column_id = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            column_header
        )

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'filter_column_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_id': column_id,
                    'operator': operator,
                    'filters': [{
                        'type': type_,
                        'condition': condition,
                        'value': value
                    }]
                }
            }
        )
    
    def filters(
            self, 
            sheet_index, 
            column_header,
            operator,
            filters
        ):

        column_id = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            column_header
        )


        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'filter_column_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_id': column_id,
                    'operator': operator,
                    'filters': filters
                }
            }
        )
    
    def sort(
            self, 
            sheet_index, 
            column_header,
            sort_direction
        ):

        column_id = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            column_header
        )

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'sort_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_id': column_id,
                    'sort_direction': sort_direction
                }
            }
        )

    def reorder_column(
            self, 
            sheet_index, 
            column_header, 
            new_column_index
        ):

        column_id = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            column_header
        )

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'reorder_column_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_id': column_id,
                    'new_column_index': new_column_index
                }
            }
        )

    def rename_column(self, sheet_index: int, old_column_header: str, new_column_header):

        column_id = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            old_column_header
        )

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'rename_column_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_id': column_id,
                    'new_column_header': new_column_header
                }
            }
        )

    def delete_columns(self, sheet_index: int, column_headers: List[str]):
        column_ids = [self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            column_header 
        ) for column_header in column_headers]

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'delete_column_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_ids': column_ids,
                }
            }
        )

    def change_column_dtype(self, sheet_index: int, column_header: str, new_dtype: str):

        column_id = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            column_header
        )

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'change_column_dtype_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_id': column_id,
                    'new_dtype': new_dtype
                }
            }
        )

    def simple_import(self, file_names: List[str]):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'simple_import_edit',
                'step_id': get_new_id(),
                'params': {
                    'file_names': file_names
                }
            }
        )

    def excel_import(self, file_name: str, sheet_names: List[str], has_headers: bool, skiprows: int):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'excel_import_edit',
                'step_id': get_new_id(),
                'params': {
                    'file_name': file_name,
                    'sheet_names': sheet_names,
                    'has_headers': has_headers,
                    'skiprows': skiprows,
                }   
            }
        )

    def bulk_old_rename(self, move_to_deprecated_id_algorithm=False):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'old_rename_only_use_this_in_testing',
                'step_id': get_new_id(),
                'params': {
                    'move_to_deprecated_id_algorithm': move_to_deprecated_id_algorithm
                }
            }
        )

    
    def undo(self):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'update_event',
                'id': get_new_id(),
                'type': 'undo'
            }
        )
    
    def redo(self):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'update_event',
                'id': get_new_id(),
                'type': 'redo'
            }
        )

    def clear(self):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'update_event',
                'id': get_new_id(),
                'type': 'clear'
            }
        )
    
    def save_analysis(self, analysis_name):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'update_event',
                'id': get_new_id(),
                'type': 'save_analysis_update',
                'analysis_name': analysis_name
            }
        )


    def rename_analysis(self, old_analysis_name, new_analysis_name):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'update_event',
                'id': get_new_id(),
                'type': 'rename_analysis_update',
                'old_analysis_name': old_analysis_name,
                'new_analysis_name': new_analysis_name
            }
        )

    
    def delete_analysis(self, analysis_name):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'update_event',
                'id': get_new_id(),
                'type': 'delete_analysis_update',
                'analysis_name': analysis_name
            }
        )

    def delete_dataframe(self, sheet_index):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'dataframe_delete_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index
                }
            }
        )

    def duplicate_dataframe(self, sheet_index):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'dataframe_duplicate_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                }
            }
        )

    def rename_dataframe(self, sheet_index, new_dataframe_name):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'dataframe_rename_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'new_dataframe_name': new_dataframe_name
                }
            }
        )

    def set_cell_value(self, sheet_index, column_header, row_index, new_value):
        column_id = self.mito_widget.steps_manager.curr_step.column_ids.get_column_id_by_header(
            sheet_index,
            column_header
        )

        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'edit_event',
                'id': get_new_id(),
                'type': 'set_cell_value_edit',
                'step_id': get_new_id(),
                'params': {
                    'sheet_index': sheet_index,
                    'column_id': column_id,
                    'row_index': row_index,
                    'new_value': str(new_value)
                }
            }
        )

    def replay_analysis(self, analysis_name, import_summaries=None, clear_existing_analysis=False):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'update_event',
                'id': get_new_id(),
                'type': 'replay_analysis_update',
                'analysis_name': analysis_name,
                'import_summaries': import_summaries,
                'clear_existing_analysis': clear_existing_analysis
            }
        )

    def checkout_step_by_idx(self, index):
        return self.mito_widget.receive_message(
            self.mito_widget,
            {
                'event': 'update_event',
                'id': get_new_id(),
                'type': 'checkout_step_by_idx_update',
                'step_idx': index,
            }
        )

    def get_sheet_data_str(self, sheet_index: int, starting_row_index: int=0):
        """
        Returns a series object of the given column, or a list if
        as_list is True. 

        Errors if the column does not exist. 
        """
        return get_sheet_data(
            {
                'event': 'api_call',
                'id': get_new_id(),
                'type': 'get_sheet_data',
                'sheet_index': sheet_index,
                'starting_row_index': starting_row_index
            },
            self.mito_widget.steps_manager
        )

    def get_formula(self, sheet_index: int, column_header: str):
        """
        Gets the formula for a given column. Returns an empty
        string if nothing exists.
        """
        column_id = self.mito_widget.steps_manager.curr_step.post_state.column_ids.get_column_id_by_header(
            sheet_index, column_header
        )
        if column_id not in self.mito_widget.steps_manager.curr_step.column_spreadsheet_code[sheet_index]:
            return ''
        return self.mito_widget.steps_manager.curr_step.column_spreadsheet_code[sheet_index][column_id]

    def get_python_formula(self, sheet_index: int, column_header: str):
        """
        Gets the formula for a given column. Returns an empty
        string if nothing exists.
        """
        column_id = self.mito_widget.steps_manager.curr_step.post_state.column_ids.get_column_id_by_header(
            sheet_index, column_header
        )
        if column_id not in self.mito_widget.steps_manager.curr_step.column_python_code[sheet_index]:
            return ''
        return self.mito_widget.steps_manager.curr_step.column_python_code[sheet_index][column_id]

    def get_value(self, sheet_index: int, column_header: str, row: int):
        """
        Returns a value in a given dataframe at the a given
        index in a column. NOTE: the row is 1 indexed!

        Errors if the value does not exist
        """
        return self.mito_widget.steps_manager.curr_step.dfs[sheet_index].at[row - 1, column_header]

    def get_column(self, sheet_index: int, column_header: str, as_list: bool):
        """
        Returns a series object of the given column, or a list if
        as_list is True. 

        Errors if the column does not exist. 
        """
        if as_list:
            return self.mito_widget.steps_manager.dfs[sheet_index][column_header].tolist()
        return self.mito_widget.steps_manager.dfs[sheet_index][column_header]
        

def create_mito_wrapper(sheet_one_A_data, sheet_two_A_data=None) -> MitoWidgetTestWrapper:
    """
    Returns a MitoWidgetTestWrapper instance wrapped around a MitoWidget
    that contains just a column A, containing sheet_one_A_data.
    
    If sheet_two_A_data is defined, then also creates a second dataframe
    with column A defined as this as well.
    """
    dfs = [pd.DataFrame(data={'A': sheet_one_A_data})]

    if sheet_two_A_data is not None:
        dfs.append(pd.DataFrame(data={'A': sheet_two_A_data}))

    mito_widget = sheet(*dfs)
    return MitoWidgetTestWrapper(mito_widget)

def create_mito_wrapper_dfs(*args):
    """
    Creates a MitoWidgetTestWrapper with a mito instance with the given
    data frames.
    """
    mito_widget = sheet(*args)
    return MitoWidgetTestWrapper(mito_widget)
