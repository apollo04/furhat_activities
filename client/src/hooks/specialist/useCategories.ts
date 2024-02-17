import { AxiosError, AxiosResponse } from 'axios';
import { useQuery, UseQueryResult } from 'react-query';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useCategories(): UseQueryResult<
  AxiosResponse<any[]>,
  AxiosError<{ message: string }>
> {
  const getCategories = () => {
    return axiosUnauthorizedInstance.get(`/categories`);
  };

  return useQuery(['categories'], getCategories);
}
