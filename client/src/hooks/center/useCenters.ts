import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { useQuery, UseQueryResult } from 'react-query';
import { Center } from 'types/generated';

export default function useCenter(): UseQueryResult<
  AxiosResponse<Center[]>,
  AxiosError<{ message: string }>
> {
  const client = useClient();

  const getCenter = () => {
    return client.get(`admins/center`);
  };

  return useQuery(['centers'], getCenter);
}
