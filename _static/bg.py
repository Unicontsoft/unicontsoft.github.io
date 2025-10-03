# This file is part of rinohtype, the Python document preparation system.
#
# Copyright (c) Brecht Machiels.
#
# Use of this source code is subject to the terms of the GNU Affero General
# Public License v3. See the LICENSE file or http://www.gnu.org/licenses/.


from .cls import Language


BG = Language('bg', 'Български',
    paragraph='Параграф',
    section='Секция',
    chapter='Глава',
    figure='Фиг.',
    table='Таблица',
    listing='Листинг',
    contents='Съдържание',
    list_of_figures='Списък фигури',
    list_of_tables='Списък таблици',
    index='Индекс',

    # admonitions
    attention='Внимание!',
    caution='Внимание!',
    danger='!ОПАСНОСТ!',
    error='Грешка',
    hint='Подсказка',
    important='Важно',
    note='Бележка',
    tip='Съвет',
    warning='Предупреждение',
    seealso='Виж също',
)
