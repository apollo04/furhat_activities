import { useEffect, useState } from 'react';

import {
  Autocomplete,
  AutocompleteItem,
  AutocompleteProps,
  Loader,
} from '@mantine/core';
import useChildren from 'hooks/children/useChildren';
import { DynamicAutoCompleteValue } from 'types';
import { Child } from 'types/generated';

interface ChildAutocompleteProps
  extends Omit<AutocompleteProps, 'data' | 'value' | 'onChange'> {
  value: DynamicAutoCompleteValue;
  onChange: (item: DynamicAutoCompleteValue | null) => void;
}

const ChildrenAutocomplete = ({
  icon,
  disabled,
  error,
  value,
  onChange,
  ...autocompleteProps
}: ChildAutocompleteProps) => {
  const [options, setOptions] = useState<AutocompleteItem[]>([]);
  const [search, setSearch] = useState(value.label);

  const { data, isLoading, isSuccess, isError } = useChildren();

  const handleSearchChange = (query: string): void => {
    setSearch(query);
    onChange(null);
  };
  const handleItemSubmit = (item: DynamicAutoCompleteValue): void => {
    setSearch('');
    onChange(item);
  };
  const handleClearSearch = (): void => {
    setSearch('');
  };

  useEffect(() => {
    if (isSuccess && data?.data) {
      setOptions(
        data.data.children.map((child: Child) => ({
          // eslint-disable-next-line no-underscore-dangle
          value: child.id,
          label: [child.name, child.surname].join(' '),
        })),
      );
    }
  }, [isSuccess, data?.data]);

  return (
    <Autocomplete
      data={options}
      value={value.label || search}
      onChange={handleSearchChange}
      onItemSubmit={handleItemSubmit}
      onDropdownClose={handleClearSearch}
      filter={(_value, _item) =>
        _item.label.toLowerCase().includes(_value.toLowerCase().trim())
      }
      icon={isLoading ? <Loader size='sm' /> : icon}
      disabled={isError || disabled}
      error={isError ? 'Something went wrong while fetching' : error}
      nothingFound={
        isLoading
          ? 'Children are loading'
          : `Children with name "${search}" are not found`
      }
      {...autocompleteProps}
    />
  );
};

export default ChildrenAutocomplete;
