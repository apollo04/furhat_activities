import { useEffect, useState } from 'react';

import {
  Autocomplete,
  AutocompleteItem,
  AutocompleteProps,
  Loader,
} from '@mantine/core';
import useCenter from 'hooks/center/useCenters';
import { DynamicAutoCompleteValue } from 'types';
import { Center } from 'types/generated';

interface CenterAutocompleteProps
  extends Omit<AutocompleteProps, 'data' | 'value' | 'onChange'> {
  value: DynamicAutoCompleteValue;
  onChange: (item: DynamicAutoCompleteValue | null) => void;
}

const CenterAutocomplete = ({
  icon,
  disabled,
  error,
  value,
  onChange,
  ...autocompleteProps
}: CenterAutocompleteProps) => {
  const [options, setOptions] = useState<AutocompleteItem[]>([]);
  const [search, setSearch] = useState(value.label);

  const { data, isLoading, isSuccess, isError } = useCenter();

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
        data.data.map((center: Center) => ({
          // eslint-disable-next-line no-underscore-dangle
          value: center._id,
          label: [center.name, center.street, center.city, center.country].join(
            ', ',
          ),
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
          ? 'Centers are loading'
          : `Centers with name "${search}" are not found`
      }
      {...autocompleteProps}
    />
  );
};

export default CenterAutocomplete;
