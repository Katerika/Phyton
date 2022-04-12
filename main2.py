from collections import Counter


class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value


def get_code(root, d=dict(), val=''):
  if root is None:
    return

  if isinstance(root.value, str):
    d[root.value] = val
    return d

  get_code(root.left, d, val + '0')
  get_code(root.right, d, val + '1')

  return d


def get_tree(string):
  str_count = Counter(string)
  if len(str_count) <= 1:
    node = Node(None)

    if len(str_count) == 1:
      node.left = Node([i for i in str_count][0])
      node.right = Node(None)

    str_count = {node: 1}

  while len(str_count) != 1:
    node = Node(None)
    spam = str_count.most_common()[:-3:-1]
    if isinstance(spam[0][0], str):
      node.left = Node(spam[0][0])

    else:
      node.left = spam[0][0]

    if isinstance(spam[1][0], str):
      node.right = Node(spam[1][0])

    else:
      node.right = spam[1][0]

    del str_count[spam[0][0]]
    del str_count[spam[1][0]]
    str_count[node] = spam[0][1] + spam[1][1]

  return [i for i in str_count][0]


def coding(str, d):
  res = ''
  for s in str:
    res += d[s]

  return res

str_1 = input('Введите строку из 3 слов: ')
tree = get_tree(str_1)

codes = get_code(tree)
print(f'Шифр: {codes}')

coding_str = coding(str_1, codes)
print(f'Закодированная строка: {coding_str}')