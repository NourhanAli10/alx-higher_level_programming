#include <Python.h>
/**
* print_python_list_info - some basic info about Python lists
* @p: PyObject
*/
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *object;
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);


	for (i = 0; i < size; i++)
	{
		object = list->ob_item[i];
		printf("Element %d: %s\n", i, Py_TYPE(object)->tp_name);
	}
}
