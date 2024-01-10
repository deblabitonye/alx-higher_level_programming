#include <Python.h>


/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p) {
printf("[.] string object info\n");

    
if (!PyUnicode_Check(p)) {
printf("  [ERROR] Invalid String Object\n");
return;
}

Py_ssize_t length = PyUnicode_GET_LENGTH(p);
const char *value = PyUnicode_AsUTF8(p);

int is_ascii = PyUnicode_IS_ASCII(p);
const char *type_str = is_ascii ? "compact ascii" : "compact unicode object";

printf("  type: %s\n", type_str);
printf("  length: %zd\n", length);
printf("  value: %s\n", value);
}
