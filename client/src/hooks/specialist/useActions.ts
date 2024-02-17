import { AxiosError, AxiosResponse } from 'axios';
import { useQuery, UseQueryResult } from 'react-query';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useActions(category: string): UseQueryResult<
  AxiosResponse<any[]>,
  AxiosError<{ message: string }>
> {
  const getActions = () => {
    return axiosUnauthorizedInstance.get(`/categories/${category}/actions`);
  };

  return useQuery(['actions', category], getActions);
}
