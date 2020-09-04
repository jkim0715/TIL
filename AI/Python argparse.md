## argparse (argument parser )

> 커멘드라인에서 들어오는 추가 입력을 받아 파이썬으로 작성된 프로그램에 해당 인자를 전달하여 실행할 수 있게 도와주는 라이브러리 입니다.

[참고](https://realpython.com/command-line-interfaces-python-argparse/)

The Python `argparse` library:

- Allows the use of positional arguments
- Allows the customization of the prefix chars
- Supports variable numbers of parameters for a single option
- Supports subcommands (A main command line parser can use other command line parsers depending on some arguments.)

**Terminologies** 

- An **argument** is a single part of a command line, delimited by blanks.
- An **option** is a particular type of argument (or a part of an argument) that can modify the behavior of the command line.
- A **parameter** is a particular type of argument that provides additional information to a single option or command

examples 

```shell
$ ls -l -s -k /var/log
```

In this example, you have five different arguments:

1. **`ls`:** the name of the command you are executing
2. **`-l`:** an option to enable the long list format
3. **`-s`:** an option to print the allocated size of each file
4. **`-k`:** an option to have the size in kilobytes
5. **`/var/log`:** a parameter that provides additional information (the path to list) to the command

### 사용법

Using the Python `argparse` library has four steps:

1. Import the Python `argparse` library
2. Create the parser
3. Add optional and positional arguments to the parser
4. Execute `.parse_args()`



- ##### Setting the Name of the Program 

  `prog`

  ```python
  # Create the parser
  my_parser = argparse.ArgumentParser(prog='myls',
                                      description='List the content of a folder')
  ```

  ```shell
  $ python myls.py
  usage: myls [-h] path
  myls.py: error: the following arguments are required: path
  ```

  As you can see, now the program name is just `myls` instead of `myls.py`.

- ##### Displaying a Custom Program Usage Help

  `usage`

  ```python
  # Create the parser
  my_parser = argparse.ArgumentParser(prog='myls',
                                      usage='%(prog)s [options] path',
                                      description='List the content of a folder')
  ```

- ##### Displaying Text Before and After the Arguments Help

  1. **`description`:** for the text that is shown before the help text
  2. **`epilog`:** for the text shown after the help text

- ##### Setting the Name or Flags of the Arguments

  There are basically two different types of arguments that you can add to your command line interface:

  1. Positional arguments
  2. Optional arguments

  ```shell
  $ cp [OPTION]... [-T] SOURCE DEST
  ```

  - `source` & `DEST` are positional arguments

  Syntactically, the difference between positional and optional arguments is that optional arguments start with `-` or `--`, while positional arguments don’t.

  To add an optional argument, you just need to call `.add_argument()` again and name the new argument with a starting `-`.

- ##### Setting the Action to Be Taken for an Argument

  - **`store`** stores the input value to the `Namespace` object. (This is the default action.)
  - **`store_const`** stores a constant value when the corresponding optional arguments are specified.
  - **`store_true`** stores the Boolean value `True` when the corresponding optional argument is specified and stores a `False` elsewhere.
  - **`store_false`** stores the Boolean value `False` when the corresponding optional argument is specified and stores `True` elsewhere.
  - **`append`** stores a list, appending a value to the list each time the option is provided.
  - **`append_const`** stores a list appending a constant value to the list each time the option is provided.
  - **`count`** stores an `int` that is equal to the times the option has been provided.
  - **`help`** shows a help text and exits.
  - **`version`** shows the version of the program and exits.

