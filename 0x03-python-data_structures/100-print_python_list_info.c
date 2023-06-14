#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print python list information
 * @p: input Python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t l_idx, len, allocated;
	PyObject *item;

	if (p == NULL || !PyList_Check(p))
		return;

	len = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", allocated);

	for (l_idx = 0; l_idx < len; l_idx++)
	{
		item = PyList_GetItem(p, l_idx);
		printf("Element %ld: %s\n", l_idx, Py_TYPE(item)->tp_name);
	}
}

