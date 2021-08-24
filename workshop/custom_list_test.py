from custom_list import CustomList
import unittest


class CustomListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_list = CustomList(1,2,3)

    def test_init(self):
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3])

    def test_append_adds_element_at_the_end(self):
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3])
        self.assertNotEqual(self.custom_list._CustomList__values[-1],5)
        self.custom_list.append(5)
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3,5])
        self.assertEqual(self.custom_list._CustomList__values[-1],5)

    def test_append_adds_if_list_is_empty(self):
        self.custom_list = CustomList()
        self.assertEqual(self.custom_list._CustomList__values, [])
        self.custom_list.append(5)
        self.assertEqual(self.custom_list._CustomList__values,[5])

    def test_append_without_value_raises(self):
        # try to call without argument but it is required
        with self.assertRaises(TypeError) as ex:
            self.custom_list.append()
        self.assertIn('append()', str(ex.exception))

    def test_append_does_not_return_value(self):
        self.assertEqual(self.custom_list.append(5),None)
    
    def test_remove_removes_element(self):
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3])
        self.assertEqual(self.custom_list._CustomList__values[0],1)
        self.custom_list.remove(0)
        self.assertEqual(self.custom_list._CustomList__values,[2,3])
        self.assertEqual(self.custom_list._CustomList__values[0],2)

    def test_remove_with_invalid_index_raises(self):
        # calls the method with invalid index
        with self.assertRaises(IndexError) as ex:
            self.custom_list.remove(100)
        self.assertEqual('Invalid index',str(ex.exception))

    def test_remove_returns_the_removed_element(self):
        self.assertEqual(self.custom_list.remove(1),2)

    def test_get_returns_correct_index(self):
        self.assertEqual(self.custom_list.get(2),3)

    def test_get_with_invalid_or_no_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.custom_list.get(100)
        self.assertIn('index',str(ex.exception))

    def test_extend_appends_iterable_to_values(self):
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3])
        self.custom_list.extend([3,4,5])
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3,3,4,5])
        self.custom_list.extend((100,200))
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3,3,4,5,100,200])
        self.custom_list.extend({5,6})
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3,3,4,5,100,200,5,6])
    
    def test_extend_appends_to_empty_list(self):
        self.custom_list = CustomList()
        self.custom_list.extend([1,2])
        self.assertEqual(self.custom_list._CustomList__values,[1,2])
    
    def test_extend_appends_non_iterable(self):
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3])
        self.custom_list.extend(5)
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3,5])

    def test_returns_new_list_and_modifies_old(self):
        res = self.custom_list.extend([100,200])
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3,100,200])
        self.assertEqual(res,[1,2,3,100,200])
        self.assertNotEqual(id(res),id(self.custom_list._CustomList__values))

    def test_insert_adds_element_to_index_shifts_others_to_right(self):
        self.assertEqual(self.custom_list._CustomList__values,[1,2,3])
        self.assertEqual(self.custom_list._CustomList__values[0],1)
        self.custom_list.insert(0,5)
        self.assertEqual(self.custom_list._CustomList__values,[5,1,2,3])
        self.assertEqual(self.custom_list._CustomList__values[0],5)
        self.assertEqual(self.custom_list._CustomList__values[1],1)
    
    def test_insert_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.custom_list.insert(100,4)
        self.assertEqual('Invalid index',str(ex.exception))
    
    def test_insert_returns_the_same_list_ref(self):
        res = self.custom_list.insert(1,6)
        self.assertEqual(res,[1,6,2,3])
        self.assertEqual(id(res),id(self.custom_list._CustomList__values))

    def test_pop_returns_last_value(self):
        self.assertEqual([1,2,3],self.custom_list._CustomList__values)
        self.assertEqual(3,self.custom_list.pop())
        self.assertEqual([1,2],self.custom_list._CustomList__values)

    def test_pop_empty_list_raises(self):
        self.custom_list = CustomList()
        with self.assertRaises(IndexError) as ex:
            self.custom_list.pop()
        self.assertIn('empty list',str(ex.exception))

    def test_clear_removes_all_elements_from_list_if_any_and_returns_none(self):
        self.assertEqual(self.custom_list.clear(),None)
        self.assertEqual(self.custom_list._CustomList__values,[])
    
    def test_index_returns_index_of_given_value(self):
        self.assertEqual(self.custom_list.index(2),1)

    def test_index_non_existant_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.index(199)
        self.assertIn('not in list',str(ex.exception))
    
    def test_count_returns_times_value_in_list(self):
        self.custom_list = CustomList(1,1,1,2,3,4)
        self.assertEqual(self.custom_list.count(1),3)
    
    def test_count_returns_null_if_value_not_in_list(self):
        self.assertEqual(self.custom_list.count(0),0)
    
    def test_reverse_returns_list_in_reverse_order_with_same_id(self):
        res = self.custom_list.reverse()
        self.assertEqual(self.custom_list.reverse(),[3,2,1])
        self.assertNotEqual(id(res),id(self.custom_list.reverse()))

    def test_copy_returns_new_reference(self):
        res = self.custom_list.copy()
        self.assertEqual(res._CustomList__values,self.custom_list._CustomList__values)
        self.assertNotEqual(id(res),id(self.custom_list))

    def test_size_returns_length_of_list_or_null(self):
        self.assertEqual(self.custom_list.size(),3)
        self.custom_list = CustomList()
        self.assertEqual(self.custom_list.size(),0)
    
    def test_add_first_adds_element_to_the_beginning(self):
        self.assertEqual(self.custom_list._CustomList__values[0],1)
        self.assertEqual(self.custom_list.add_first(100),None)
        self.assertEqual(self.custom_list._CustomList__values,[100,1,2,3])
        self.assertEqual(self.custom_list._CustomList__values[0],100)
    
    def test_dictionize_with_even_values(self):
        self.custom_list = CustomList(1,2,3,4)
        res = self.custom_list.dictionize()
        self.assertTrue(isinstance(res,dict))
        self.assertEqual(res,{1:2,3:4})

    def test_dictionize_with_odd_values(self):
        res = self.custom_list.dictionize()
        self.assertEqual(res,{1:2,3: ' '})
    
    def test_move_amount_of_elements_to_end_of_list_returns_list(self):
        self.assertEqual(self.custom_list.move(2),[3,1,2])
        self.assertEqual(self.custom_list.move(0),[3,1,2])
        self.assertEqual(self.custom_list.move(3),[3,1,2])
    
    def test_move_higher_amount_than_list_raises(self):
        with self.assertRaises(Exception) as ex:
            self.custom_list.move(4)
        self.assertEqual(
            'You\'re trying to move more elements than the list contains',
            str(ex.exception))
    
    def test_sum_raise_if_object_does_not_implement_dunder_len(self):
        class Person:
            pass
        self.custom_list = CustomList(1,2,3,Person())
        with self.assertRaises(Exception) as ex:
            self.custom_list.sum()
        self.assertEqual('Person object doesent have length',str(ex.exception))

    def test_sum_returns_sum_of_integers_floats_and_iterables_with_only_numbers(self):
        self.custom_list = CustomList(1.5,3,4,[2,3.5,3])
        self.assertEqual(self.custom_list.sum(),17.0)

    def test_sum_returns_sum_of_numbers_and_length_of_non_number_objects(self):
        self.custom_list = CustomList(1.5,3,4,[2,3.5,3],'asd',('a',3),{'b':4,'c':5,'d':6})
        self.assertEqual(self.custom_list.sum(),25.0)
    
    def test_sum_works_with_only_non_number_objects_or_no_objects(self):
        self.custom_list = CustomList('hello')
        self.assertEqual(self.custom_list.sum(),5)
        self.custom_list = CustomList()
        self.assertEqual(self.custom_list.sum(),0)

    def test_overbound_returns_max_element_value(self):
        self.custom_list = CustomList(1,2.4,[1,2,3],'asdf')
        self.assertEqual(self.custom_list.overbound(),3)
        self.assertEquals(self.custom_list._CustomList__values[3],'asdf')
    
    def test_overbound_raises_if_object_has_no_value_or_len(self):
        class Person:
            pass
        self.custom_list = CustomList(1,2.4,'asd',Person())
        with self.assertRaises(Exception) as ex:
            self.custom_list.overbound()
        self.assertEqual('Person object doesent have a value',str(ex.exception))

    def test_overbound_returns_first_object_if_objects_have_equal_value(self):
        self.custom_list = CustomList(1,1,1)
        self.assertEqual(self.custom_list.overbound(),0)

    def test_underbound_returns_max_element_value(self):
        self.custom_list = CustomList(1,2.4,[1,2,3],'asdf')
        self.assertEqual(self.custom_list.underbound(),0)
        self.assertEquals(self.custom_list._CustomList__values[0],1)
    
    def test_underbound_raises_if_object_has_no_value_or_len(self):
        class Person:
            pass
        self.custom_list = CustomList(1,2.4,'asd',Person())
        with self.assertRaises(Exception) as ex:
            self.custom_list.underbound()
        self.assertEqual('Person object doesent have a value',str(ex.exception))

    def test_underbound_returns_first_object_if_objects_have_equal_value(self):
        self.custom_list = CustomList(1,1,1)
        self.assertEqual(self.custom_list.underbound(),0)

if __name__ == '__main__':
    unittest.main()